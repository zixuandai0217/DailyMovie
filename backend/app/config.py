from pydantic_settings import BaseSettings
from functools import lru_cache
from pathlib import Path


class Settings(BaseSettings):
    APP_NAME: str = "DailyMovie API"
    DEBUG: bool = True
    API_V1_PREFIX: str = "/api/v1"

    # TMDB API 配置
    TMDB_API_KEY: str
    TMDB_ACCESS_TOKEN: str
    TMDB_BASE_URL: str = "https://api.themoviedb.org/3"
    TMDB_IMAGE_BASE_URL: str = "https://image.tmdb.org/t/p"

    # GLM (AI) 配置
    GLM_API_KEY: str = ""
    GLM_BASE_URL: str = "https://open.bigmodel.cn/api/anthropic"

    # 数据库配置
    DATABASE_URL: str = "sqlite+aiosqlite:///./data/daily_movie.db"

    # CORS 配置
    CORS_ORIGINS: list[str] = ["http://localhost:5173", "http://localhost:3000"]

    class Config:
        # .env 文件在项目根目录
        env_file = str(Path(__file__).parent.parent.parent / ".env")
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    return Settings()