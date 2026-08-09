from typing import List
from pydantic_settings import BaseSettings
from pydantic import field_validator


class Settings(BaseSettings):
    DATABASE_URL: str
    API_PREFIX: str = "\api"
    DEBUG: bool = False
    ALLOWED_ORIGINS: List[str] = ""
    OPENAI_API_KEY: str

    @field_validator("ALLOWED_ORIGINS")
    @classmethod
    def parse_allowed_origins(cls, v: str) -> List[str]:
        return [origin.strip() for origin in v.split(",") if origin.strip()]