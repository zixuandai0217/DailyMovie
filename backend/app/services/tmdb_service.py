import httpx
import asyncio
from typing import Optional, Dict, Any, List
from app.config import get_settings

settings = get_settings()


class TMDBService:
    """TMDB API 服务"""

    def __init__(self):
        self.base_url = settings.TMDB_BASE_URL
        self.api_key = settings.TMDB_API_KEY
        self.access_token = settings.TMDB_ACCESS_TOKEN
        self.image_base_url = settings.TMDB_IMAGE_BASE_URL

    def _get_headers(self) -> Dict[str, str]:
        return {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json;charset=utf-8",
        }

    async def _request(
        self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """通用请求方法"""
        url = f"{self.base_url}/{endpoint}"
        params = params or {}
        params["api_key"] = self.api_key

        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params, headers=self._get_headers(), timeout=30.0)
            response.raise_for_status()
            return response.json()

    async def get_random_movie(self) -> Optional[Dict[str, Any]]:
        """获取随机电影 - 从热门电影中随机选择"""
        data = await self._request("movie/popular", {"page": 1, "language": "zh-CN"})
        movies = data.get("results", [])
        if movies:
            import random
            movie = random.choice(movies)
            return await self.get_movie_details(movie["id"])
        return None

    async def get_movie_details(self, movie_id: int) -> Dict[str, Any]:
        """获取电影详情"""
        # 并行请求中文和英文数据
        task_zh = self._request(f"movie/{movie_id}", {
            "language": "zh-CN",
            "append_to_response": "credits"
        })
        task_en = self._request(f"movie/{movie_id}", {
            "language": "en-US"
        })

        data, data_en = await asyncio.gather(task_zh, task_en)

        # 提取导演
        director = None
        for crew in data.get("credits", {}).get("crew", []):
            if crew.get("job") == "Director":
                director = crew.get("name")
                break

        # 提取主演（取前5名）
        cast_list = [actor.get("name") for actor in data.get("credits", {}).get("cast", [])[:5]]

        # 处理类型
        genres = [g["name"] for g in data.get("genres", [])]

        return {
            "tmdb_id": data["id"],
            "title": data["title"],
            "title_en": data_en.get("title"),
            "original_title": data.get("original_title"),
            "overview": data.get("overview"),
            "overview_en": data_en.get("overview"),
            "homepage": data.get("homepage"),
            "poster_path": data.get("poster_path"),
            "backdrop_path": data.get("backdrop_path"),
            "release_date": data.get("release_date"),
            "vote_average": data.get("vote_average", 0),
            "genres": genres,
            "runtime": data.get("runtime"),
            "tagline": data.get("tagline"),
            "director": director,
            "cast": cast_list,
        }

    async def search_movies(self, query: str, page: int = 1) -> Dict[str, Any]:
        """搜索电影"""
        return await self._request("search/movie", {"query": query, "page": page, "language": "zh-CN"})


tmdb_service = TMDBService()
