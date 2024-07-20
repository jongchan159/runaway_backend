from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Runaway App"
    PROJECT_VERSION: str = "1.0.0"
    MONGODB_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

settings = Settings()