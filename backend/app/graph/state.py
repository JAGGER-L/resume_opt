from typing import Literal, TypedDict

from app.schemas.gap import GapAnalysis
from app.schemas.interview import InterviewQuestion
from app.schemas.jd import JDAnalysis
from app.schemas.resume import ResumeAnalysis, ResumeVersion
from app.schemas.review import ResumeReview


class ResumeGraphState(TypedDict, total=False):
    job_id: str
    thread_id: str
    user_id: str | None
    language: Literal["zh", "en"]
    job_description: str
    resume_text: str
    jd_analysis: JDAnalysis
    resume_analysis: ResumeAnalysis
    gap_analysis: GapAnalysis
    resume_versions: list[ResumeVersion]
    review: ResumeReview
    interview_questions: list[InterviewQuestion]
    markdown_export: str
    warnings: list[str]
