from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str = "dev"
    STATIC_API_KEY: str = "dev"

    APP_NAME: str = "secunda"
    APP_DESCRIPTION: str = "Secunda API"

    # Database
    SQLALCHEMY_DATABASE_URL: str = "postgres://docker:docker@localhost:47744/secunda"

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()