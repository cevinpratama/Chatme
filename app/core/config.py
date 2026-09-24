from pydantic_settings import BaseSettings
class Settings:
    PROJECT_NAME = "Project Chatme Cevin"
    API_V1_STR: str = "/api/v1"

    AI_APIKEY : str

    class Config:
        env_file = ".env"

settings = Settings()