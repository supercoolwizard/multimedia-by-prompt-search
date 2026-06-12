from pathlib import Path
from settings import TARGET_DIR

for file in TARGET_DIR.iterdir():
    print(file)
