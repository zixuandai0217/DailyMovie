import json
import httpx
from typing import Dict, Any
from app.config import get_settings
from app.services.tmdb_service import tmdb_service

settings = get_settings()

class AIService:
    def __init__(self):
        self.api_key = settings.GLM_API_KEY
        self.base_url = settings.GLM_BASE_URL
        
    async def get_search_params(self, prompt: str) -> Dict[str, Any]:
        """
        Analyze user prompt and return TMDB search parameters.
        Returns JSON with: { "genres": [ids], "keywords": [str], "year_start": int, "year_end": int, "sort_by": str }
        """
        # Get genre mapping first
        try:
            genre_map = await tmdb_service.get_genres()
            genre_str = ", ".join([f"{k}:{v}" for k, v in genre_map.items()])
        except Exception:
            genre_str = "Action: 28, Comedy: 35, Drama: 18" # Fallback

        system_prompt = f"""
        You are a movie recommendation assistant. Your goal is to convert user natural language requests into structured parameters for the TMDB API.
        
        Available Genres (Name:ID): {genre_str}
        
        Output valid JSON only. No markdown.
        Fields:
        - genres: list of genre IDs (integers)
        - year_start: int or null
        - year_end: int or null
        - sort_by: "popularity.desc", "vote_average.desc", "release_date.desc" (default: popularity.desc)
        
        Example: "I want a sad romantic movie from the 90s"
        Output: {{"genres": [10749, 18], "year_start": 1990, "year_end": 1999, "sort_by": "popularity.desc"}}
        """
        
        messages = [
            {"role": "user", "content": prompt}
        ]
        
        headers = {
            "x-api-key": self.api_key,
            "authorization": f"Bearer {self.api_key}",
            "content-type": "application/json",
            "anthropic-version": "2023-06-01"
        }
        
        url = f"{self.base_url}/messages"
        
        payload = {
            "model": "glm-4", 
            "messages": messages,
            "system": system_prompt,
            "max_tokens": 1024,
            "temperature": 0.5
        }
        
        async with httpx.AsyncClient() as client:
            try:
                resp = await client.post(url, json=payload, headers=headers, timeout=30.0)
                resp.raise_for_status()
                data = resp.json()
                content = data["content"][0]["text"]
                
                # Extract JSON from content
                if "```json" in content:
                    content = content.split("```json")[1].split("```")[0].strip()
                elif "```" in content:
                    content = content.split("```")[1].strip()
                    
                return json.loads(content)
            except Exception as e:
                print(f"AI Service Error: {e}")
                return {}

    async def recommend_movies(self, prompt: str) -> Dict[str, Any]:
        params = await self.get_search_params(prompt)
        
        # Construct TMDB query
        tmdb_params = {
            "page": 1,
            "sort_by": params.get("sort_by", "popularity.desc")
        }
        
        if params.get("genres"):
            tmdb_params["with_genres"] = ",".join(map(str, params.get("genres")))
            
        if params.get("year_start"):
            tmdb_params["primary_release_date.gte"] = f"{params['year_start']}-01-01"
            
        if params.get("year_end"):
            tmdb_params["primary_release_date.lte"] = f"{params['year_end']}-12-31"
            
        return await tmdb_service.discover_movies(**tmdb_params)

ai_service = AIService()
