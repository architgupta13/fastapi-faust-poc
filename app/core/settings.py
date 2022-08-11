from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    PROJECT_NAME: str = "fastapi-faust-poc"

    # Kafka config
    KAFKA_BROKER_URL: str = Field(..., env="KAFKA_BROKER_URL")
    KAFKA_USERNAME: str = Field(..., env="KAFKA_USERNAME")
    KAFKA_PASSWORD: str = Field(..., env="KAFKA_PASSWORD")

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
