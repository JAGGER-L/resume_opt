from pydantic import BaseModel, ConfigDict, Field


class ResumeReview(BaseModel):
    model_config = ConfigDict(extra="ignore")

    passed: bool = True
    ats_score: int = Field(default=0, ge=0, le=100)
    language_score: int = Field(default=0, ge=0, le=100)
    unsupported_claims: list[str] = Field(default_factory=list)
    revision_notes: list[str] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)
