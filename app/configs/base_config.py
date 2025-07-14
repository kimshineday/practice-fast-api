from enum import StrEnum

from pydantic_settings import BaseSettings, SettingsConfigDict


class Env(StrEnum):
    LOCAL = "local"
    STAGE = "stage"
    PROD = "prod"


class Config(BaseSettings):
    ENV: Env = Env.LOCAL  # 환경 변수

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    MYSQL_HOST: str = "localhost"
    MYSQL_PORT: int = 3306
    MYSQL_USER: str = "root"
    MYSQL_PASSWORD: str
    MYSQL_DB: str = "when2meet"
    MYSQL_CONNECT_TIMEOUT: int = 5
    CONNECTION_POOL_MAXSIZE: int = 30
