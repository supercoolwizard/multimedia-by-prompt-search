from pathlib import Path

class MultimediaTypeFinder:
    IMAGE_EXTENSIONS = {
        ".jpg", ".jpeg", ".png", ".gif",
        ".bmp", ".webp", ".tif", ".tiff", ".svg"
    }

    VIDEO_EXTENSIONS = {
        ".mp4", ".mov", ".avi", ".mkv",
        ".webm", ".wmv", ".flv", ".m4v"
    }

    def find_type(self, path):
        path = Path(path)

        if not path.is_file():
            return None

        ext = path.suffix.lower()

        if ext in self.IMAGE_EXTENSIONS:
            return "image"

        if ext in self.VIDEO_EXTENSIONS:
            return "video"

        return None
