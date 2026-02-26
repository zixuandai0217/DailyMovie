# Index Page Layout Adjustment Plan

> **For Trae:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development to implement this plan task-by-task.

**Goal:** Adjust the layout of the index page to reduce the movie poster size and ensure the description text is partially visible without scrolling.

**Architecture:** Modify CSS styles to constrain image height and adjust container layout.

**Tech Stack:** WXML, WXSS

---

### Task 1: Update Image Mode and Height

**Files:**
- Modify: `miniprogram/pages/index/index.wxml`
- Modify: `miniprogram/pages/index/index.wxss`

**Step 1: Change Image Mode in WXML**

Modify `miniprogram/pages/index/index.wxml`:
- Change `<image ... mode="widthFix">` to `<image ... mode="aspectFill">`.
- This ensures the image covers the area without distorting, allowing us to set a fixed height.

**Step 2: Update CSS for Poster and Card**

Modify `miniprogram/pages/index/index.wxss`:
- Update `.poster`:
  - Set `height: 800rpx;` (or similar fixed height to take up ~60% of screen, leaving room for text).
  - Ensure `width: 100%;`.
  - Add `border-radius: 12rpx 12rpx 0 0;` (optional, for better card look).
- Update `.movie-card`:
  - Ensure it has `overflow: hidden` (already present).
  - Maybe add a `max-height` if we want to force scrolling within the card, but user just wants text "partially visible", so reducing image height is enough.

**Verification:**
- Check that the image is not distorted.
- Check that the title and at least the first few lines of the overview are visible on a standard screen (simulated).
