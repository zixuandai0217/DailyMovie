# DailyMovie Mini Program Redesign Plan

## 1. Overview

Redesign the WeChat Mini Program to include a 3-tab navigation structure, adding AI recommendations and user personalization features. This involves both frontend UI changes and backend database updates.

## 2. Navigation Structure (Tab Bar)

- **Tab 1: Today (今日推荐)**
  - Current "Home" page.
  - Shows a random movie card.
  - Pull-to-refresh for new recommendation.
- **Tab 2: AI Recommender (AI荐片)**
  - **New Page**.
  - Interface: Chat-like input or form for user to describe what they want to watch.
  - Output: List of recommended movies based on the prompt.
- **Tab 3: My Profile (我的喜好)**
  - **New Page**.
  - **Unauthenticated State**: "Login" button (WeChat Login).
  - **Authenticated State**:
    - User Info (Avatar, Nickname).
    - "My Preferences" form (Genres, Eras, Keywords).
    - "My Favorites" list (Saved movies).

## 3. Backend Changes

### Database Models (`backend/app/models/database.py`)

- **User**:
  - `id`: Integer (Primary Key)
  - `openid`: String (WeChat OpenID, Unique)
  - `nickname`: String
  - `avatar_url`: String
  - `created_at`: DateTime
- **UserPreference**:
  - `user_id`: ForeignKey(User.id)
  - `favorite_genres`: JSON/String (List of genre IDs)
  - `preferred_decades`: JSON/String (e.g., ["1990s", "2000s"])
  - `keywords`: String

### API Endpoints (`backend/app/api/`)

- **Auth**: `POST /api/v1/auth/wechat` - Exchange code for token/session.
- **User**: `GET /api/v1/user/profile`, `PUT /api/v1/user/preferences`.
- **AI**: Update `POST /api/v1/ai/recommend` to accept `user_id` context if available.

## 4. Frontend Implementation Plan

1.  **Update `app.json`**: Configure the 3 tabs and new page paths.
2.  **Create Pages**:
    - `pages/ai/index`: Input area + Result list.
    - `pages/profile/index`: Login state + Form.
3.  **Implement Auth**:
    - Use `wx.login()` to get code.
    - Send code to backend to create/retrieve user.
    - Store session token in `wx.setStorage`.
4.  **Connect AI**:
    - Call existing `/api/v1/ai/recommend` endpoint.

## 5. Next Steps

- [ ] Create backend models for User.
- [ ] Implement WeChat login endpoint.
- [ ] Update Mini Program `app.json` and create page shells.
