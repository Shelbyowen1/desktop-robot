import os
from PIL import Image

input_folder = "raw_pngs"
output_folder = "circuitpy_files"

# Target dimensions (change to (240, 320) if mounting vertically)
TARGET_SIZE = (320, 240)

os.makedirs(output_folder, exist_ok=True)

#loops through pngs
for filename in os.listdir(input_folder):
    if filename.lower().endswith(".png"):
        img_path = os.path.join(input_folder, filename)
        
        # Open, resize to exact screen dimensions, and convert to standard 24-bit RGB
        img = Image.open(img_path).resize(TARGET_SIZE).convert("RGB")
        
        # Grab just the name without .png and save as .bmp
        base_name = os.path.splitext(filename)[0]
        out_path = os.path.join(output_folder, f"{base_name}.bmp")
        img.save(out_path)
        print(f"Converted: {filename} -> {base_name}.bmp")

print("Done!")
