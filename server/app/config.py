from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql+psycopg2://postgres:postgres@postgres-db:5432/dev"
    echo_sql: bool = True
    test: bool = False
    project_name: str = "Simple Python and FastAPI API"
    oauth_token_secret: str = "secret"
    log_level: str = "DEBUG"


settings = Settings()
