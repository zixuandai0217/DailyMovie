import os
from PIL import Image

# #7c4dff = (124, 77, 255)
TARGET_COLOR = (124, 77, 255) 

# Assuming script is in d:\Code\DailyMovie\backend\scripts
# Images are in d:\Code\DailyMovie\miniprogram\images
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, '../../miniprogram/images'))

FILES = ['home_active.png', 'ai_active.png', 'user_active.png']

def recolor_icon(path):
    try:
        if not os.path.exists(path):
            print(f"File not found: {path}")
            return False

        print(f"Processing {path}...")
        img = Image.open(path).convert("RGBA")
        
        # Get data
        data = img.getdata()
        
        new_data = []
        for item in data:
            # item is (r, g, b, a)
            # If pixel is not transparent (alpha > 0), change color
            if item[3] > 0:
                # Use target color, keep original alpha
                # To be safer, we can check if it's already close to target, 
                # but here we just blindly recolor all non-transparent pixels 
                # which works for flat icons.
                new_data.append((*TARGET_COLOR, item[3]))
            else:
                new_data.append(item)
        
        img.putdata(new_data)
        img.save(path, "PNG")
        print(f"Successfully saved {path}")
        return True
    except Exception as e:
        print(f"Error processing {path}: {e}")
        return False

def main():
    print(f"Target Images Directory: {IMAGES_DIR}")
    
    if not os.path.exists(IMAGES_DIR):
        print("Images directory does not exist!")
        return

    for filename in FILES:
        full_path = os.path.join(IMAGES_DIR, filename)
        recolor_icon(full_path)

if __name__ == "__main__":
    main()
