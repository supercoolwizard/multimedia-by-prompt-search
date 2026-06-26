import os
import platform
import subprocess


class PlatformFileRevealer:
    def reveal_file(self, path):
        path = os.path.abspath(path)
        system = platform.system()

        if system == "Darwin":  # macOS
            subprocess.run(["open", "-R", path])

        elif system == "Windows":
            subprocess.run(["explorer", f"/select,{path}"])

        else:  # Linux
            subprocess.run(["xdg-open", os.path.dirname(path)])

