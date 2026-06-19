import subprocess

class VideoSlicer:
    def __init__(self):
        pass

    def get_video_duration(self, path):
        result = subprocess.run(
            [
                "ffprobe",
                "-v", "error",
                "-show_entries", "format=duration",
                "-of", "default=noprint_wrappers=1:nokey=1",
                path,
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        return float(result.stdout.strip())

    def slice(self, video_path):
        duration = self.get_video_duration(video_path)
        return [0, duration]
