"""
path: app/config.py

# MySQL
MYSQL_USER=demo
MYSQL_PASSWORD=demo@123
MYSQL_SERVER=localhost
MSQL_PORT=3306
MYSQL_DATABASE=demo_db
"""

import os
from pathlib import Path
from urllib.parse import quote_plus
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

ENV_PATH = Path('.') / '.env'
load_dotenv(dotenv_path=ENV_PATH)


class Settings(BaseSettings):
    """
    Settings class
    """
    DATABASE_USER: str = os.getenv("MYSQL_USER")
    DATABASE_PASSWORD: str = os.getenv("MYSQL_PASSWORD")
    DATABASE_SERVER: str = os.getenv("MYSQL_SERVER")
    # DATABASE_PORT: str = int(os.getenv("MYSQL_PORT"))
    DATABASE_NAME: str = os.getenv("MYSQL_DATABASE")
    DATABASE_URL: str = "sqlite:///dev.db"

    class Config:
        """
        Config class
        """
        case_sensitive = True


settings = Settings()
