from app.graph import prompts
from app.graph.state import ResumeGraphState
from app.llm import LLMClient
from app.schemas.resume import ResumeVersionsPayload


def generate_resumes_node(state: ResumeGraphState, llm: LLMClient) -> ResumeGraphState:
    language = state["language"]
    payload = llm.invoke_model(
        ResumeVersionsPayload,
        prompts.system_prompt(language),
        prompts.versions_user_prompt(
            state["jd_analysis"],
            state["resume_analysis"],
            state["gap_analysis"],
            prompts.schema_text(ResumeVersionsPayload),
        ),
    )
    versions = payload.versions[:3]
    if len(versions) != 3:
        raise RuntimeError("LLM must return exactly 3 resume versions.")
    return {"resume_versions": versions}
