import requests

class FastVLMClient:
    def describe(self, image_path):
        with open(image_path, "rb") as f:
            response = requests.post(
                "http://fastvlm:8000/describe",
                files={"image": f}
            )

        response.raise_for_status()
        return response.json()["description"]
