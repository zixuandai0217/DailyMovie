# Bilingual Movie Info & Font Improvement Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Enable bilingual (Chinese/English) display for movie titles and overviews, and improve frontend typography.

**Architecture:**
- Backend: Update `TMDBService` to fetch both Chinese and English data (parallel requests). Update `MovieResponse` schema to include English fields.
- Frontend: Update API types and `HomeView` to display bilingual content. Integrate Google Fonts for better typography.

**Tech Stack:** FastAPI, Python, Vue 3, TypeScript, CSS (Google Fonts).

---

### Task 1: Backend - Bilingual Data Fetching

**Files:**
- Modify: `backend/app/models/schemas.py`
- Modify: `backend/app/services/tmdb_service.py`

**Step 1: Update Schema**
Add `title_en` and `overview_en` to `MovieResponse`.

```python
# backend/app/models/schemas.py
class MovieResponse(BaseModel):
    # ... existing fields
    title_en: Optional[str] = None
    overview_en: Optional[str] = None
```

**Step 2: Update TMDB Service**
Modify `get_movie_details` to fetch both languages.

```python
# backend/app/services/tmdb_service.py
# Use asyncio.gather to fetch 'zh-CN' and 'en-US' versions.
# Merge results: use zh for main fields, extract title/overview from en response.
```

**Step 3: Verification**
- Create a test script or use `curl` to check `/api/v1/movies/random` response.
- Verify `title_en` and `overview_en` are present.

### Task 2: Frontend - Bilingual Display & Fonts

**Files:**
- Modify: `frontend/src/api/movie.ts`
- Modify: `frontend/index.html` (for fonts)
- Modify: `frontend/src/views/HomeView.vue`
- Modify: `frontend/src/assets/main.css` (optional, global fonts)

**Step 1: Update Frontend Types**
Update `Movie` interface in `movie.ts`.

```typescript
export interface Movie {
  // ... existing
  title_en: string | null
  overview_en: string | null
}
```

**Step 2: Add Fonts**
Add Google Fonts (e.g., Noto Sans SC, Montserrat) to `frontend/index.html`.

```html
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&family=Noto+Sans+SC:wght@400;700&display=swap" rel="stylesheet">
```

**Step 3: Update HomeView**
- Display `title_en` below `title`.
- Display `overview_en` below `overview`.
- Apply font styles:
  - Titles: `Noto Sans SC` (ZH) + `Montserrat` (EN).
  - Body: Readable sans-serif.

**Step 4: Verification**
- Run frontend.
- Check visual appearance and data correctness.
