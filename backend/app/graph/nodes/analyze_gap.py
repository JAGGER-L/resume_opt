from app.graph import prompts
from app.graph.state import ResumeGraphState
from app.llm import LLMClient
from app.schemas.gap import GapAnalysis


def analyze_gap_node(state: ResumeGraphState, llm: LLMClient) -> ResumeGraphState:
    language = state["language"]
    gap_analysis = llm.invoke_model(
        GapAnalysis,
        prompts.system_prompt(language),
        prompts.gap_user_prompt(
            state["jd_analysis"],
            state["resume_analysis"],
            prompts.schema_text(GapAnalysis),
        ),
    )
    return {"gap_analysis": gap_analysis}
