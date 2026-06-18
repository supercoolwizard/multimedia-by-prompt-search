from fastapi import FastAPI, UploadFile, File, Form
import subprocess
import tempfile
import shutil

app = FastAPI()

@app.post("/describe")
async def describe(image_path):
    cmd = [
        "python",
        "predict.py",
        "--model-path", "/models/llava-fastvithd_0.b_stage3",
        "--image-file", image_path,
        "--prompt", "Describe the image."
    ]

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        check=True
    )

    return {"description": result.stdout.strip()}
