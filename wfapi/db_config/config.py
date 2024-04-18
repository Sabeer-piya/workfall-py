import os
from functools import lru_cache
from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from typing import ClassVar

env_path = Path("") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings(BaseSettings):
    DB_USER: str = os.getenv('PlSQL_USER','postgres')
    DB_NAME: str = os.getenv('PlSQL_DB','workfall')
    DB_PASSWORD : str = os.getenv('PlSQL_PASSWORD', 'test')
    DB_HOST: str = os.getenv('PlSQL_SERVER','localhost')
    DB_PORT: str = os.getenv('PlSQL_PORT','5432')
    DATABASE_URL : ClassVar[str] = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

@lru_cache
def get_settings() -> Settings:
    return Settings()