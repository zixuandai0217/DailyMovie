# Localization to Chinese Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Translate all user-facing text in the WeChat Mini Program from English to Chinese.

**Architecture:** Directly modify WXML and JS files to replace English strings with Chinese equivalents.

**Tech Stack:** WeChat Mini Program (WXML, JS, JSON)

---

### Task 1: Update Global Configuration

**Files:**
- Modify: `d:\Code\DailyMovie\miniprogram\app.json`

**Step 1: Translate Tab Bar**
Change `tabBar.list` items:
- "Today" -> "今日"
- "AI Rec" -> "AI推荐"
- "Me" -> "我的"

**Step 2: Translate Navigation Titles**
Change `window.navigationBarTitleText` -> "每日电影" (DailyMovie)
Change other pages' navigation bar titles if defined in `app.json` (though most are custom now).

### Task 2: Update Today Tab (Index)

**Files:**
- Modify: `d:\Code\DailyMovie\miniprogram\pages\index\index.wxml`
- Modify: `d:\Code\DailyMovie\miniprogram\pages\index\index.js`

**Step 1: Translate WXML**
- "Loading..." -> "加载中..." (if present)
- "Refresh" -> "换一换" (or similar button text)

**Step 2: Translate JS**
- `wx.showLoading({ title: 'Loading...' })` -> `'加载中...'`
- `wx.showToast({ title: 'Failed to load' })` -> `'加载失败'`
- `wx.showToast({ title: 'Success' })` -> `'成功'`

### Task 3: Update AI Recommendation Tab

**Files:**
- Modify: `d:\Code\DailyMovie\miniprogram\pages\ai\index.wxml`
- Modify: `d:\Code\DailyMovie\miniprogram\pages\ai\index.js`

**Step 1: Translate WXML**
- "AI Recommendation" -> "AI 推荐"
- "Ask me anything..." / placeholder -> "告诉我你喜欢什么样的电影..."
- "Send" -> "发送"
- "Try these examples:" -> "试试这些例子："
- Empty state messages.

**Step 2: Translate JS**
- Loading/Error messages.
- Example prompts (if hardcoded in JS) -> Translate to Chinese.

### Task 4: Update Profile Tab

**Files:**
- Modify: `d:\Code\DailyMovie\miniprogram\pages\profile\index.wxml`
- Modify: `d:\Code\DailyMovie\miniprogram\pages\profile\index.js`

**Step 1: Translate WXML**
- "My Profile" -> "个人中心"
- "Start Journey" -> "开启旅程"
- "My Movie DNA" -> "我的电影基因"
- "Favorite Genres" -> "喜欢的类型"
- "Preferred Eras" -> "喜欢的年代"
- "Special Keywords" -> "特别关键词"
- Placeholder "e.g. sad, plot twist, indie" -> "例如：感人，反转，独立电影"
- "Save My DNA" -> "保存我的基因"
- "Logout" -> "退出登录"

**Step 2: Translate JS**
- `genres` names: "Action" -> "动作", "Comedy" -> "喜剧", etc.
- `eras` names: "80s" -> "80年代", etc.
- Toast messages: "Logging in..." -> "登录中...", "Login failed" -> "登录失败", "Saving..." -> "保存中...", "Saved!" -> "已保存".

### Task 5: Update Detail Page

**Files:**
- Modify: `d:\Code\DailyMovie\miniprogram\pages\detail\detail.wxml`
- Modify: `d:\Code\DailyMovie\miniprogram\pages\detail\detail.js` (if any text)

**Step 1: Translate WXML**
- "Overview" -> "简介"
- "Release Date" -> "上映日期"
- "Rating" -> "评分"
- "Cast" -> "演员"

### Task 6: Update Search Page

**Files:**
- Modify: `d:\Code\DailyMovie\miniprogram\pages\search\search.wxml`
- Modify: `d:\Code\DailyMovie\miniprogram\pages\search\search.js` (if any text)

**Step 1: Translate WXML**
- Search placeholder -> "搜索电影..."
- "No results found" -> "未找到相关电影"
