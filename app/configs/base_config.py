from enum import StrEnum
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Env(StrEnum):
    LOCAL = "local"
    STAGE = "stage"
    PROD = "prod"

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Config(BaseSettings):
    ENV: Env = Env.LOCAL  # 환경 변수
    MYSQL_HOST: str
    MYSQL_PORT: int
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_DB: str
    MYSQL_CONNECT_TIMEOUT: int
    CONNECTION_POOL_MAXSIZE: int

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding = "utf-8"
    )
