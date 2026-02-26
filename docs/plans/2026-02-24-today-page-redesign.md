# Today Page Redesign Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use subagent-driven-development to implement this plan task-by-task.

**Goal:** Redesign the "Today" page to be premium, high-end, and immersive using Glassmorphism and better typography.

**Architecture:**
- **Background:** Full-screen blurred movie poster for immersion.
- **Card:** Glassmorphism style (translucent white/dark) floating on top.
- **Typography:** Enhanced hierarchy with clear title, rating, and meta info.
- **Interactivity:** Smooth transitions and a floating action button for refresh.

**Tech Stack:** WXML, WXSS, JavaScript (WeChat Mini Program)

---

### Task 1: Update WXML Structure

**Files:**
- Modify: `miniprogram/pages/index/index.wxml`

**Step 1: Add Background Container**
- Add a `view.background-container` behind the main content.
- Inside it, place an `image` binding to `movie.poster_path` (or `backdrop_path` if available, but poster is safer).

**Step 2: Restructure Movie Card**
- Wrap the card content in a `view.glass-card`.
- Reorganize `info` section:
  - `header` (Title, Tagline).
  - `meta-row` (Rating, Date, Runtime).
  - `tags-row` (Genres).
  - `overview` (Description).

**Step 3: Update Action Button**
- Move `refresh-btn` to a floating position or better styled button inside/outside the card.

---

### Task 2: Implement Glassmorphism and Layout (WXSS)

**Files:**
- Modify: `miniprogram/pages/index/index.wxss`

**Step 1: Background Styling**
- `.background-container`: Fixed position, full width/height, z-index -1.
- `.background-image`: Width 100%, height 100%, object-fit cover, `filter: blur(30px) brightness(0.6)`.

**Step 2: Glass Card Styling**
- `.glass-card`:
  - `background: rgba(255, 255, 255, 0.85)` (for light theme) or adjust for dark.
  - `backdrop-filter: blur(20px)`.
  - `border: 1px solid rgba(255, 255, 255, 0.4)`.
  - `box-shadow: 0 30rpx 60rpx rgba(0,0,0,0.2)`.
  - `border-radius: 40rpx`.

**Step 3: Typography and Spacing**
- `.title`: Larger (56rpx), bold/heavy.
- `.tagline`: Italic, lighter color, smaller (28rpx).
- `.rating-value`: Large font, highlight color (e.g., #FFD700 or primary purple).
- `.tags`: Flex row, small pill shapes for genres.

---

### Task 3: Verify and Refine

**Files:**
- Modify: `miniprogram/pages/index/index.js` (if needed for data processing)

**Step 1: Check Data Binding**
- Ensure `genres` are displayed correctly (e.g., `wx:for="{{movie.genres}}"`).
- Handle missing data gracefully (wx:if).

**Step 2: Polish**
- Add transitions/animations for loading new movies.
