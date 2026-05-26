from pydantic import BaseModel, ConfigDict, Field


class JDAnalysis(BaseModel):
    model_config = ConfigDict(extra="ignore")

    role_title: str = ""
    seniority: str = ""
    responsibilities: list[str] = Field(default_factory=list)
    required_skills: list[str] = Field(default_factory=list)
    preferred_skills: list[str] = Field(default_factory=list)
    ats_keywords: list[str] = Field(default_factory=list)
    success_criteria: list[str] = Field(default_factory=list)
