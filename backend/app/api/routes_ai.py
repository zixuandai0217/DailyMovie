from fastapi import APIRouter, HTTPException, Body
from app.models.schemas import MovieListResponse
from app.services.ai_service import ai_service
from typing import Dict

router = APIRouter(prefix="/ai", tags=["ai"])

@router.post("/recommend", response_model=MovieListResponse)
async def ai_recommend(body: Dict[str, str] = Body(..., example={"prompt": "I want a sci-fi movie"})):
    """AI 推荐电影"""
    user_prompt = body.get("prompt")
    if not user_prompt:
        raise HTTPException(status_code=400, detail="Prompt is required")
        
    data = await ai_service.recommend_movies(user_prompt)
    
    # Transform to MovieResponse format
    movies = []
    for m in data.get("results", []):
        movies.append({
            "id": m["id"],
            "tmdb_id": m["id"],
            "title": m["title"],
            "title_en": m.get("original_title"), # 简略处理，列表页通常不强制双语
            "original_title": m.get("original_title"),
            "overview": m.get("overview"),
            "overview_en": None, 
            "poster_path": m.get("poster_path"),
            "backdrop_path": m.get("backdrop_path"),
            "release_date": m.get("release_date"),
            "vote_average": m.get("vote_average", 0),
            "genres": [], # 列表页暂时不显示详细类型名
            "homepage": None,
            "director": None,
            "cast": [],
            "runtime": None,
            "tagline": None,
            "is_favorite": False,
        })
        
    return {"movies": movies, "total": data.get("total_results", 0), "page": data.get("page", 1), "page_size": 20}
