"""Configuration settings for the invoice extraction project.

This module handles environment variables and configuration settings.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    groq_api_key: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


def get_settings() -> Settings:
    try:
        return Settings()
    except Exception as e:
        raise ValueError(
            "Error loading settings. "
            "Make sure GROQ_API_KEY is defined "
            "in the .env file or as an environment variable."
        ) from e

