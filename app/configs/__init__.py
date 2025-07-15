from pathlib import Path

from app.configs.base_config import Config


def get_config() -> Config:
    project_root = Path(__file__).resolve().parent.parent.parent
    env_file = project_root / ".env"
    return Config(_env_file=(env_file), _env_file_encoding="utf-8")


config = get_config()
