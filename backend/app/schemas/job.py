from enum import StrEnum
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

from app.schemas.export import MarkdownExport
from app.schemas.gap import GapAnalysis
from app.schemas.interview import InterviewQuestion
from app.schemas.jd import JDAnalysis
from app.schemas.resume import ResumeAnalysis, ResumeVersion
from app.schemas.review import ResumeReview


class JobStatus(StrEnum):
    pending = "pending"
    running = "running"
    completed = "completed"
    failed = "failed"


class OptimizeRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    job_description: str = Field(min_length=20)
    resume_text: str = Field(min_length=20)
    language: Literal["zh", "en"] = "zh"
    user_id: str | None = None


class ResumeOptimizationResult(BaseModel):
    model_config = ConfigDict(extra="ignore")

    language: Literal["zh", "en"]
    jd_analysis: JDAnalysis
    resume_analysis: ResumeAnalysis
    gap_analysis: GapAnalysis
    resume_versions: list[ResumeVersion]
    review: ResumeReview
    interview_questions: list[InterviewQuestion]
    markdown_export: MarkdownExport
    warnings: list[str] = Field(default_factory=list)


class OptimizeResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    job_id: str
    user_id: str | None = None
    status: JobStatus
    result: ResumeOptimizationResult | None = None
    error: str | None = None
