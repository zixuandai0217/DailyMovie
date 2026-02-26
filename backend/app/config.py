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
    # Use absolute path to ensure it works regardless of CWD
    DATABASE_URL: str = f"sqlite+aiosqlite:///{Path(__file__).parent.parent.parent.joinpath('data', 'daily_movie.db').as_posix()}"

    # CORS 配置
    # 小程序在开发环境下使用微信 IDE 调试，不需要配置 CORS
    # 真机预览/上线需要配置为你的线上域名
    CORS_ORIGINS: list[str] = [
        "http://localhost:5173",
        "http://localhost:3000",
        "http://192.168.3.245:5173",
    ]

    class Config:
        # .env 文件在项目根目录
        env_file = str(Path(__file__).parent.parent.parent / ".env")
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    return Settings()