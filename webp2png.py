import sys
import os
from PIL import Image

def get_application_path():
    if getattr(sys, 'frozen', False):
        # If the application is run as a bundle (e.g., by PyInstaller)
        application_path = os.path.dirname(sys.executable)
    else:
        # If the application is run as a normal Python script
        application_path = os.path.dirname(os.path.abspath(__file__))
    return application_path

def convert_webp_to_png(webp_filepath):
    try:
        if not os.path.isfile(webp_filepath):
            return None

        if not webp_filepath.lower().endswith(".webp"):
            return None

        app_dir = get_application_path()
        filename_without_ext = os.path.splitext(os.path.basename(webp_filepath))[0]
        png_filename = filename_without_ext + ".png"
        png_filepath = os.path.join(app_dir, png_filename)

        img = Image.open(webp_filepath)
        img.save(png_filepath, "PNG")
        
        return png_filepath

    except Exception:
        return None

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        convert_webp_to_png(input_file)
    # No else block, no instructions printed