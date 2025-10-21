from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str = "dev"
    STATIC_API_KEY: str = "dev"

    # Database
    DATABASE_URL: str = "postgresql://user:password@db:5432/organization_db"

    class Config:
        case_sensitive = True


settings = Settings()