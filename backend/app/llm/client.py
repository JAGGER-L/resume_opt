import json
from typing import Any, TypeVar

from pydantic import BaseModel, ValidationError

from app.config import Settings

T = TypeVar("T", bound=BaseModel)


class LLMClient:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    def invoke_json(self, system_prompt: str, user_prompt: str) -> dict[str, Any]:
        if not self.settings.deepseek_api_key:
            raise RuntimeError("DEEPSEEK_API_KEY is required to call the configured LLM.")

        from openai import OpenAI

        client = OpenAI(
            api_key=self.settings.deepseek_api_key,
            base_url=self.settings.deepseek_base_url,
            timeout=self.settings.llm_timeout_seconds,
        )
        response = client.chat.completions.create(
            model=self.settings.default_model,
            temperature=self.settings.llm_temperature,
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )
        content = response.choices[0].message.content or ""
        return self._parse_json(content)

    def invoke_model(self, model_type: type[T], system_prompt: str, user_prompt: str) -> T:
        payload = self.invoke_json(system_prompt, user_prompt)
        try:
            return model_type.model_validate(payload)
        except ValidationError as exc:
            raise RuntimeError(f"LLM returned invalid {model_type.__name__}: {exc}") from exc

    @staticmethod
    def _parse_json(content: str) -> dict[str, Any]:
        text = content.strip()
        if text.startswith("```"):
            lines = text.splitlines()
            if lines and lines[0].startswith("```"):
                lines = lines[1:]
            if lines and lines[-1].startswith("```"):
                lines = lines[:-1]
            text = "\n".join(lines).strip()

        try:
            parsed = json.loads(text)
        except json.JSONDecodeError as exc:
            raise RuntimeError("LLM did not return valid JSON.") from exc
        if not isinstance(parsed, dict):
            raise RuntimeError("LLM JSON response must be an object.")
        return parsed
