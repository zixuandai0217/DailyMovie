# Fix Keyword Input Interaction Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Improve the interaction of the "Special Keywords" input field to ensure users can edit it easily, addressing the "seems selected/can't change" issue.

**Architecture:** Use WeChat Mini Program's `model:value` for two-way binding and programmatic focus management to expand the clickable area.

**Tech Stack:** WeChat Mini Program (WXML, WXSS, JS)

---

### Task 1: Enhance Input Focus and Binding

**Files:**
- Modify: `d:\Code\DailyMovie\miniprogram\pages\profile\index.js`
- Modify: `d:\Code\DailyMovie\miniprogram\pages\profile\index.wxml`

**Step 1: Add focus state logic to JS**

In `d:\Code\DailyMovie\miniprogram\pages\profile\index.js`:
1.  Add `inputFocus: false` to `data`.
2.  Add `focusInput()` method:
    ```javascript
    focusInput() {
      this.setData({ inputFocus: true });
    },
    ```
3.  Remove `onKeywordInput` method (as we will use `model:value`).

**Step 2: Update WXML for binding and focus**

In `d:\Code\DailyMovie\miniprogram\pages\profile\index.wxml`:
1.  Add `bindtap="focusInput"` to the `.input-card` container.
2.  Update `<input>`:
    - Add `focus="{{inputFocus}}"`
    - Change `value="{{keywords}}"` to `model:value="{{keywords}}"`
    - Remove `bindinput="onKeywordInput"`
    - Ensure `cursor-spacing="20"` (to prevent keyboard covering input, though container has padding)

**Step 3: Verify**
- Since we can't run the simulator, rely on code correctness for MP API usage.
- Check logic: Tapping anywhere on the card sets `inputFocus` to true -> input gets focus -> keyboard opens.
- Check binding: Typing updates `this.data.keywords` automatically via `model:value`.

### Task 2: Ensure Visual Clarity

**Files:**
- Modify: `d:\Code\DailyMovie\miniprogram\pages\profile\index.wxss`

**Step 1: Ensure text color visibility**

In `d:\Code\DailyMovie\miniprogram\pages\profile\index.wxss`:
1.  Explicitly set `color: #333` on `.input`.
2.  Add `height: 100%` to `.input` to fill vertical space if flex doesn't handle it perfectly (optional, but safer).

```css
.input {
  /* ... existing styles ... */
  color: #333;
  height: 100%;
}
```
