from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PRODUCTION: bool
    APP_TITLE: str
    DESCRIPTION: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    DATABASE_URL: str
    SECRET_WORD: str = "SECRET"
    ADMIN_AUTH_SECRET_KEY: str = "SECRET"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
