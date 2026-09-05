from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    environment: str = "local"
    database_url: str = "postgresql://postgres:postgres@localhost:5432/jobintel"

    jwt_secret: str = "changeme"
    jwt_algorithm: str = "HS256"
    jwt_expiry_minutes: int = 60

    # Local disk storage for Phase 1. Swappable for S3 later (see storage.py).
    resume_storage_dir: str = "storage/resumes"
    resume_max_size_mb: int = 5
    resume_allowed_types: tuple[str, ...] = ("application/pdf",
                                              "application/vnd.openxmlformats-officedocument.wordprocessingml.document")

    # Comma-separated list of allowed frontend origins. Defaults cover local dev.
    cors_allowed_origins: list[str] = ["http://localhost:3000", "http://127.0.0.1:3000"]

    cors_allowed_origins: list[str] = ["http://localhost:3000"]

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
