from app.graph import prompts
from app.graph.state import ResumeGraphState
from app.llm import LLMClient
from app.schemas.jd import JDAnalysis


def analyze_jd_node(state: ResumeGraphState, llm: LLMClient) -> ResumeGraphState:
    language = state["language"]
    jd_analysis = llm.invoke_model(
        JDAnalysis,
        prompts.system_prompt(language),
        prompts.jd_user_prompt(state["job_description"], prompts.schema_text(JDAnalysis)),
    )
    return {"jd_analysis": jd_analysis}
