from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    PROJECT_NAME: str = "Project Chatme Cevin"
    API_V1_STR: str = "/api/v1"

    AI_APIKEY : str

    model_config = SettingsConfigDict(env_file = ".env", extra="ignore")

settings = Settings()