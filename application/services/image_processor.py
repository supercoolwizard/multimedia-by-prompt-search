from domain.multimedia import Multimedia
from application.services.multimedia_processor import MultimediaProcessorStrategy
from PIL import Image


class ImageProcessor(MultimediaProcessorStrategy):
    def __init__(self, describer, encoder):
        self.describer = describer
        self.encoder = encoder
        self.prompt = "This is an image, describe it in detail."

    def image_preprocessor(self, image_path):
        image = Image.open(image_path).convert("RGB")
        return image

    def process(self, image_path, id):
        image = self.image_preprocessor(image_path)
        description = self.describer.describe(image, self.prompt)
        vector = self.encoder.encode(description)

        metadata = {
            "path": image_path,
            "text_description": description,
            "entity_type": "image"
        }

        image_data = Multimedia(
            id=id,
            vector=vector,
            metadata=metadata,
        )

        return [image_data]
