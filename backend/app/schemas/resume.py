from pydantic import BaseModel, ConfigDict, Field


class ResumeAnalysis(BaseModel):
    model_config = ConfigDict(extra="ignore")

    candidate_summary: str = ""
    experience_facts: list[str] = Field(default_factory=list)
    project_facts: list[str] = Field(default_factory=list)
    education_facts: list[str] = Field(default_factory=list)
    skill_facts: list[str] = Field(default_factory=list)
    source_facts: list[str] = Field(default_factory=list)
    risk_notes: list[str] = Field(default_factory=list)


class ResumeVersion(BaseModel):
    model_config = ConfigDict(extra="ignore")

    version_id: str
    name: str
    strategy: str
    target_focus: list[str] = Field(default_factory=list)
    resume_markdown: str
    source_fact_refs: list[str] = Field(default_factory=list)
    packaging_notes: list[str] = Field(default_factory=list)
    risk_notes: list[str] = Field(default_factory=list)


class ResumeVersionsPayload(BaseModel):
    model_config = ConfigDict(extra="ignore")

    versions: list[ResumeVersion] = Field(default_factory=list)
