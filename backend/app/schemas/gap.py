from pydantic import BaseModel, ConfigDict, Field


class GapAnalysis(BaseModel):
    model_config = ConfigDict(extra="ignore")

    match_score: int = Field(default=0, ge=0, le=100)
    strong_matches: list[str] = Field(default_factory=list)
    missing_requirements: list[str] = Field(default_factory=list)
    transferable_strengths: list[str] = Field(default_factory=list)
    optimization_suggestions: list[str] = Field(default_factory=list)
    risk_points: list[str] = Field(default_factory=list)
