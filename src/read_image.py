from pathlib import Path

from PIL import Image


def read_image(image_path):
    """Read a JPG/JPEG image from disk and return it as an RGB Pillow image."""
    path = Path(image_path)

    try:
        with Image.open(path) as image:
            return image.convert("RGB")
    except FileNotFoundError:
        raise
    except OSError as exc:
        raise ValueError(f"Could not read image: {path}") from exc
