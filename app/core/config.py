from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '../../.env')
load_dotenv(dotenv_path)

class Settings(BaseSettings):
    GOOGLE_API_KEY: str = os.getenv('GOOGLE_API_KEY')
    POSTGRES_DB_URL: str = os.getenv('POSTGRES_DB_URL')
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000

settings = Settings()