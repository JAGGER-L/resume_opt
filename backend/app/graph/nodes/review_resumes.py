from app.graph import prompts
from app.graph.state import ResumeGraphState
from app.llm import LLMClient
from app.schemas.review import ResumeReview


def review_resumes_node(state: ResumeGraphState, llm: LLMClient) -> ResumeGraphState:
    language = state["language"]
    review = llm.invoke_model(
        ResumeReview,
        prompts.system_prompt(language),
        prompts.review_user_prompt(
            state["jd_analysis"],
            state["resume_analysis"],
            state["resume_versions"],
            prompts.schema_text(ResumeReview),
        ),
    )
    warnings = list(state.get("warnings", []))
    warnings.extend(review.warnings)
    warnings.extend(review.unsupported_claims)
    return {"review": review, "warnings": warnings}
