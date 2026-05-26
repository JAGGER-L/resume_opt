from dataclasses import dataclass
from functools import lru_cache
from uuid import uuid4

from app.config import get_settings
from app.graph.builder import build_resume_graph
from app.llm import LLMClient
from app.schemas.export import MarkdownExport
from app.schemas.job import (
    JobStatus,
    OptimizeRequest,
    OptimizeResponse,
    ResumeOptimizationResult,
)
from app.services.exporter import MarkdownExporter


@dataclass
class JobRecord:
    job_id: str
    user_id: str | None
    status: JobStatus
    result: ResumeOptimizationResult | None = None
    error: str | None = None


class InMemoryJobStore:
    def __init__(self) -> None:
        self._jobs: dict[str, JobRecord] = {}

    def save(self, record: JobRecord) -> None:
        self._jobs[record.job_id] = record

    def get(self, job_id: str) -> JobRecord | None:
        return self._jobs.get(job_id)


class JobService:
    def __init__(self, store: InMemoryJobStore, llm: LLMClient, exporter: MarkdownExporter) -> None:
        self.store = store
        self.graph = build_resume_graph(llm=llm, exporter=exporter)

    def optimize(self, request: OptimizeRequest) -> OptimizeResponse:
        job_id = str(uuid4())
        user_id = request.user_id
        record = JobRecord(job_id=job_id, user_id=user_id, status=JobStatus.running)
        self.store.save(record)

        try:
            state = self.graph.invoke(
                {
                    "job_id": job_id,
                    "thread_id": job_id,
                    "user_id": user_id,
                    "language": request.language,
                    "job_description": request.job_description,
                    "resume_text": request.resume_text,
                    "warnings": [],
                },
                config={"configurable": {"thread_id": job_id}},
            )
            result = ResumeOptimizationResult(
                language=request.language,
                jd_analysis=state["jd_analysis"],
                resume_analysis=state["resume_analysis"],
                gap_analysis=state["gap_analysis"],
                resume_versions=state["resume_versions"],
                review=state["review"],
                interview_questions=state["interview_questions"],
                markdown_export=MarkdownExport(
                    filename=f"resume_optimization_{job_id}.md",
                    content=state["markdown_export"],
                ),
                warnings=state.get("warnings", []),
            )
            record.status = JobStatus.completed
            record.result = result
            self.store.save(record)
            return OptimizeResponse(job_id=job_id, user_id=user_id, status=record.status, result=result)
        except Exception as exc:
            record.status = JobStatus.failed
            record.error = str(exc)
            self.store.save(record)
            raise

    def get_job(self, job_id: str) -> OptimizeResponse | None:
        record = self.store.get(job_id)
        if record is None:
            return None
        return OptimizeResponse(
            job_id=record.job_id,
            user_id=record.user_id,
            status=record.status,
            result=record.result,
            error=record.error,
        )


@lru_cache
def get_job_service() -> JobService:
    settings = get_settings()
    return JobService(
        store=InMemoryJobStore(),
        llm=LLMClient(settings),
        exporter=MarkdownExporter(),
    )
