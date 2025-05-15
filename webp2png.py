import sys
import os
from PIL import Image

def convert_webp_to_png(webp_filepath):
    try:
        if not os.path.isfile(webp_filepath):
            return
        if not webp_filepath.lower().endswith(".webp"):
            return

        directory = os.path.dirname(webp_filepath)
        filename_without_ext = os.path.splitext(os.path.basename(webp_filepath))[0]
        png_filepath = os.path.join(directory, filename_without_ext + ".png")

        img = Image.open(webp_filepath)
        img.save(png_filepath, "PNG")
    except Exception:
        pass

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        convert_webp_to_png(input_file)