from pydantic import BaseModel, ConfigDict, Field


class InterviewQuestion(BaseModel):
    model_config = ConfigDict(extra="ignore")

    question: str
    why_it_matters: str
    answer_framework: list[str] = Field(default_factory=list)
    evidence_to_prepare: list[str] = Field(default_factory=list)


class InterviewPayload(BaseModel):
    model_config = ConfigDict(extra="ignore")

    questions: list[InterviewQuestion] = Field(default_factory=list)
