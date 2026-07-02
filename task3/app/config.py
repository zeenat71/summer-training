from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    SECRET_KEY: str = "8gK9mP2xL7nQ5vR1sT4uW8yZ3aBcDeFg"
    DATABASE_URL: str = "sqlite:///./patients.db"

    model_config = SettingsConfigDict(
        env_file=".env"
    )


settings = Settings()