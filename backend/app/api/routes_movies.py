from fastapi import APIRouter, HTTPException
from app.models.schemas import MovieResponse, RandomMovieResponse, MovieListResponse
from app.services.tmdb_service import tmdb_service

router = APIRouter(prefix="/movies", tags=["movies"])


@router.get("/random", response_model=RandomMovieResponse)
async def get_random_movie():
    """获取随机推荐电影"""
    movie = await tmdb_service.get_random_movie()
    if not movie:
        raise HTTPException(status_code=404, detail="No movies found")
    movie_data = {**movie, "id": movie["tmdb_id"], "is_favorite": False}
    return {"movie": movie_data, "message": "每日推荐电影"}


@router.get("/{movie_id}", response_model=MovieResponse)
async def get_movie_detail(movie_id: int):
    """获取电影详情"""
    movie = await tmdb_service.get_movie_details(movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    movie_data = {**movie, "id": movie["tmdb_id"], "is_favorite": False}
    return movie_data


@router.get("/search", response_model=MovieListResponse)
async def search_movies(query: str, page: int = 1):
    """搜索电影"""
    data = await tmdb_service.search_movies(query, page)
    movies = []
    for m in data.get("results", []):
        movies.append({
            "id": m["id"],
            "tmdb_id": m["id"],
            "title": m["title"],
            "original_title": m.get("original_title"),
            "overview": m.get("overview"),
            "poster_path": m.get("poster_path"),
            "backdrop_path": m.get("backdrop_path"),
            "release_date": m.get("release_date"),
            "vote_average": m.get("vote_average", 0),
            "genres": [],
            "director": None,
            "cast": [],
            "runtime": None,
            "tagline": None,
            "is_favorite": False,
        })
    return {"movies": movies, "total": data.get("total_results", 0), "page": page, "page_size": 20}