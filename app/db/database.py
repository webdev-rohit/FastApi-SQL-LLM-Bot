from langchain.sql_database import SQLDatabase
from app.core.config import settings

db = SQLDatabase.from_uri(settings.POSTGRES_DB_URL)