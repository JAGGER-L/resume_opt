from app.graph import prompts
from app.graph.state import ResumeGraphState
from app.llm import LLMClient
from app.schemas.interview import InterviewPayload


def generate_interview_node(state: ResumeGraphState, llm: LLMClient) -> ResumeGraphState:
    language = state["language"]
    payload = llm.invoke_model(
        InterviewPayload,
        prompts.system_prompt(language),
        prompts.interview_user_prompt(
            state["jd_analysis"],
            state["resume_versions"],
            prompts.schema_text(InterviewPayload),
        ),
    )
    return {"interview_questions": payload.questions[:15]}
