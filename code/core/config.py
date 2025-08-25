from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PRODUCTION: bool = False
    APP_TITLE: str = "Notes App"
    DESCRIPTION: str = "Application for notes"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str
    DATABASE_URL: str
    SECRET_WORD: str
    ADMIN_AUTH_SECRET_KEY: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="allow",
    )


settings = Settings()
