import re

class MultimediaTypeFinder():
    def __init__(self):
        self.IMAGE_RE = re.compile(r'.*\.(?:jpg|jpeg|png|gif|bmp|webp|tiff?|svg)$', re.IGNORECASE)
        self.VIDEO_RE = re.compile(r'.*\.(?:mp4|mov|avi|mkv|webm|wmv|flv|m4v)$', re.IGNORECASE)

    def find_type(self, multimedia_path):
        if self.IMAGE_RE.match(multimedia_path):
            return "image"
        if self.VIDEO_RE.match(multimedia_path):
            return "video"
