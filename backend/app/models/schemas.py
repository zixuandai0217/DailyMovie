from pydantic import BaseModel
from typing import Optional, List


class MovieResponse(BaseModel):
    """电影响应模型"""
    id: int
    tmdb_id: int
    title: str
    title_en: Optional[str] = None
    original_title: Optional[str] = None
    overview: Optional[str] = None
    overview_en: Optional[str] = None
    homepage: Optional[str] = None
    poster_path: Optional[str] = None
    backdrop_path: Optional[str] = None
    release_date: Optional[str] = None
    vote_average: float = 0
    genres: List[str] = []
    director: Optional[str] = None
    cast: List[str] = []
    runtime: Optional[int] = None
    tagline: Optional[str] = None
    is_favorite: bool = False

    class Config:
        from_attributes = True


class RandomMovieResponse(BaseModel):
    """随机电影响应"""
    movie: MovieResponse
    message: str = "每日推荐电影"


class MovieListResponse(BaseModel):
    """电影列表响应"""
    movies: List[MovieResponse]
    total: int
    page: int
    page_size: int