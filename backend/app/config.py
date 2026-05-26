from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "resume_opt"
    environment: str = "local"

    default_llm_provider: Literal["deepseek"] = "deepseek"
    default_model: str = "deepseek-chat"
    deepseek_api_key: str = Field(default="", repr=False)
    deepseek_base_url: str = "https://api.deepseek.com"
    llm_temperature: float = 0.2
    llm_timeout_seconds: int = 120


@lru_cache
def get_settings() -> Settings:
    return Settings()
