import json
from typing import Literal

from pydantic import BaseModel


LANGUAGE_LABELS = {
    "zh": "Chinese",
    "en": "English",
}


def schema_text(model: type[BaseModel]) -> str:
    return json.dumps(model.model_json_schema(), ensure_ascii=False, indent=2)


def system_prompt(language: Literal["zh", "en"]) -> str:
    return f"""
You are a rigorous resume optimization assistant.
Return only a valid JSON object. Do not wrap the JSON in Markdown.
Output language must be {LANGUAGE_LABELS[language]}.

Rules:
- Reasonable packaging is allowed: rewrite, reorganize, emphasize transferable strengths,
  and use conservative wording for impact.
- Do not invent companies, titles, dates, degrees, certifications, projects, tools,
  metrics, awards, or responsibilities that are not supported by the resume text.
- If a metric is not provided, use qualitative impact language instead of fabricating numbers.
- Preserve factual traceability: mention which source facts support generated resume content.
""".strip()


def jd_user_prompt(job_description: str, output_schema: str) -> str:
    return f"""
Analyze this job description and extract structured hiring signals.

JSON schema:
{output_schema}

Job description:
{job_description}
""".strip()


def resume_user_prompt(resume_text: str, output_schema: str) -> str:
    return f"""
Analyze this resume. Extract only facts that are explicitly present or strongly supported.

JSON schema:
{output_schema}

Resume:
{resume_text}
""".strip()


def gap_user_prompt(jd_analysis: BaseModel, resume_analysis: BaseModel, output_schema: str) -> str:
    return f"""
Compare the JD analysis with the resume analysis. Identify match quality, gaps, risks,
and optimization suggestions.

JSON schema:
{output_schema}

JD analysis:
{jd_analysis.model_dump_json(indent=2)}

Resume analysis:
{resume_analysis.model_dump_json(indent=2)}
""".strip()


def versions_user_prompt(
    jd_analysis: BaseModel,
    resume_analysis: BaseModel,
    gap_analysis: BaseModel,
    output_schema: str,
) -> str:
    return f"""
Generate exactly 3 tailored resume versions:
1. ATS keyword coverage version
2. Achievement-oriented version
3. Role-fit version

Each version must be complete Markdown resume content. Keep unsupported claims out of the resume.

JSON schema:
{output_schema}

JD analysis:
{jd_analysis.model_dump_json(indent=2)}

Resume analysis:
{resume_analysis.model_dump_json(indent=2)}

Gap analysis:
{gap_analysis.model_dump_json(indent=2)}
""".strip()


def review_user_prompt(
    jd_analysis: BaseModel,
    resume_analysis: BaseModel,
    versions: list[BaseModel],
    output_schema: str,
) -> str:
    versions_json = json.dumps(
        [version.model_dump(mode="json") for version in versions],
        ensure_ascii=False,
        indent=2,
    )
    return f"""
Review the optimized resume versions. Check ATS relevance, language quality, and unsupported claims.
Flag any claim that cannot be traced back to the resume analysis.

JSON schema:
{output_schema}

JD analysis:
{jd_analysis.model_dump_json(indent=2)}

Resume analysis:
{resume_analysis.model_dump_json(indent=2)}

Resume versions:
{versions_json}
""".strip()


def interview_user_prompt(
    jd_analysis: BaseModel,
    resume_versions: list[BaseModel],
    output_schema: str,
) -> str:
    versions_json = json.dumps(
        [version.model_dump(mode="json") for version in resume_versions],
        ensure_ascii=False,
        indent=2,
    )
    return f"""
Generate 10 to 15 likely interview questions based on the JD and optimized resumes.
For each question, include why it matters, an answer framework, and evidence the candidate should prepare.

JSON schema:
{output_schema}

JD analysis:
{jd_analysis.model_dump_json(indent=2)}

Optimized resumes:
{versions_json}
""".strip()
