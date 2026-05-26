from app.graph import prompts
from app.graph.state import ResumeGraphState
from app.llm import LLMClient
from app.schemas.resume import ResumeAnalysis


def analyze_resume_node(state: ResumeGraphState, llm: LLMClient) -> ResumeGraphState:
    language = state["language"]
    resume_analysis = llm.invoke_model(
        ResumeAnalysis,
        prompts.system_prompt(language),
        prompts.resume_user_prompt(state["resume_text"], prompts.schema_text(ResumeAnalysis)),
    )
    return {"resume_analysis": resume_analysis}
