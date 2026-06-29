from pathlib import Path

from PIL import Image


def read_images(image_paths):
    """Read images from disk and return them as RGB Pillow images."""
    images = []

    for image_path in image_paths:
        path = Path(image_path)

        try:
            with Image.open(path) as image:
                images.append(image.convert("RGB"))
        except FileNotFoundError:
            raise
        except OSError as exc:
            raise ValueError(f"Could not read image: {path}") from exc

    return images
