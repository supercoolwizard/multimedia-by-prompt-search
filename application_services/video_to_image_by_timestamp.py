import subprocess
from pathlib import Path
import json

class VideoToImageService:
    def video_frame_to_array_ffmpeg(self, video_path, timestamp):
        """
        returns frame as RGB numpy array: shape (H, W, 3)
        """
        cmd = [
            "ffmpeg",
            "-ss", str(timestamp),
            "-i", video_path,
            "-frames:v", "1",
            "-f", "rawvideo",
            "-pix_fmt", "rgb24",
            "-"
        ]

        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        out, err = process.communicate()

        if process.returncode != 0:
            raise RuntimeError(err.decode())

        probe = subprocess.check_output([
            "ffprobe", "-v", "error",
            "-select_streams", "v:0",
            "-show_entries", "stream=width,height",
            "-of", "json",
            video_path
        ])

        info = json.loads(probe)
        w = info["streams"][0]["width"]
        h = info["streams"][0]["height"]

        frame = np.frombuffer(out, np.uint8).reshape((h, w, 3))
        return frame


    def video_to_image_by_timestamp(self, video_path, timestamp, output_path):
        """
        timestamp format is in seconds as string
        """
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)

        cmd = [
            "ffmpeg",
            "-y", 
            "-ss", str(timestamp),
            "-i", video_path,
            "-frames:v", "1",
            output_path
        ]

        subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

        return output_path
