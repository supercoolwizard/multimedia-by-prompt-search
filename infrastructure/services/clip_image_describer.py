from application.ports.image_describer import ImageDescriber
import torch
from transformers import CLIPProcessor, CLIPModel


class CLIPImageDescriber(ImageDescriber):
    DEFAULT_CANDIDATES = [
        "a photograph of a person",
        "a photograph of a group of people",
        "a portrait",
        "an animal",
        "a plant or flower",
        "a landscape or nature scene",
        "a city or urban scene",
        "a building or architecture",
        "a vehicle",
        "a piece of furniture",
        "food or a meal",
        "a product or object on a plain background",
        "a piece of art or painting",
        "an illustration or drawing",
        "a digital rendering or 3D image",
        "a screenshot of software or a website",
        "a diagram or chart",
        "a map",
        "a logo or icon",
        "a piece of text or a document",
        "an abstract image or pattern",
    ]

    def __init__(self, hf_token, config):
        self.model_name = "openai/clip-vit-base-patch32"
        self.device = config.device
        self.processor = CLIPProcessor.from_pretrained(
            self.model_name,
            token=hf_token,
        )
        self.model = CLIPModel.from_pretrained(
            self.model_name,
            torch_dtype=config.dtype,
            token=hf_token,
        ).to(self.device)

    def _candidate_descriptions(self, prompt):
        parts = [p.strip() for p in prompt.split(",") if p.strip()]
        if len(parts) > 1:
            return parts
        return self.DEFAULT_CANDIDATES

    def describe(self, image, prompt):
        candidates = self._candidate_descriptions(prompt)

        inputs = self.processor(
            images=image,
            text=candidates,
            return_tensors="pt",
            padding=True,
        )
        inputs = {k: v.to(self.device) for k, v in inputs.items()}

        with torch.inference_mode():
            outputs = self.model(**inputs)

        logits_per_image = outputs.logits_per_image
        best_idx = logits_per_image.argmax(dim=1).item()

        return candidates[best_idx]