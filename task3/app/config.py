from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    SECRET_KEY: str = "dev-secret-key-change-this"
    DATABASE_URL: str = "sqlite:///./patients.db"
    

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()