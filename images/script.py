import os
from PIL import Image

source_dir = "./fulls"
dest_dir = "./thumbs"
target_width = 512

os.makedirs(dest_dir, exist_ok=True)

for filename in os.listdir(source_dir):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.gif')):
        img_path = os.path.join(source_dir, filename)
        dest_path = os.path.join(dest_dir, filename)
        
        # Skip if the thumbnail already exists
        if os.path.exists(dest_path):
            continue
            
        with Image.open(img_path) as img:
            wpercent = (target_width / float(img.size[0]))
            target_height = int((float(img.size[1]) * float(wpercent)))
            
            img_resized = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
            img_resized.save(dest_path)
            print(f"Resized: {filename}")

print("Done! Any new images have been resized.")
