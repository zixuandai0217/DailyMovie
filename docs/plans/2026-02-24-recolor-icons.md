# Tab Bar Icon Color Update Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Recolor the active tab bar icons to match the new purple theme (#7c4dff).

**Architecture:** Use a Python script with Pillow (PIL) to process the existing PNG images, tinting non-transparent pixels to the target color.

**Tech Stack:** Python, Pillow (PIL)

---

### Task 1: Verify Environment and Dependencies

**Files:**
- Read: `d:\Code\DailyMovie\backend\pyproject.toml` (if exists) or check installed packages.

**Step 1: Check for Pillow**
Run: `uv pip list` or `pip list` in backend environment to check if `pillow` is installed.
If not, run `uv add pillow` in `backend` directory.

### Task 2: Create Recolor Script

**Files:**
- Create: `d:\Code\DailyMovie\backend\scripts\recolor_icons.py`

**Step 1: Write script**
The script will:
1. Define the target color: `#7c4dff`.
2. Define source files: `home_active.png`, `ai_active.png`, `user_active.png` in `../miniprogram/images/`.
3. Open each image.
4. Convert to RGBA.
5. Iterate over pixels: if alpha > 0, set RGB to target color, keep Alpha.
6. Save overwriting the file.

```python
import os
from PIL import Image

TARGET_COLOR = (124, 77, 255) # #7c4dff
IMAGES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../miniprogram/images'))
FILES = ['home_active.png', 'ai_active.png', 'user_active.png']

def recolor():
    print(f"Target Directory: {IMAGES_DIR}")
    for filename in FILES:
        path = os.path.join(IMAGES_DIR, filename)
        if not os.path.exists(path):
            print(f"Skipping {filename}: File not found")
            continue
            
        print(f"Processing {filename}...")
        try:
            img = Image.open(path).convert("RGBA")
            data = img.getdata()
            new_data = []
            for item in data:
                # item is (r, g, b, a)
                if item[3] > 0: # If not transparent
                    # Tint to target color, keep original alpha
                    new_data.append((*TARGET_COLOR, item[3]))
                else:
                    new_data.append(item)
            
            img.putdata(new_data)
            img.save(path, "PNG")
            print(f"Saved {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    recolor()
```

### Task 3: Execute Recolor

**Files:**
- Execute: `d:\Code\DailyMovie\backend\scripts\recolor_icons.py`

**Step 1: Run script**
Run: `uv run python scripts/recolor_icons.py` inside `backend` directory.

**Step 2: Verify**
Check output for "Saved ..." messages.
