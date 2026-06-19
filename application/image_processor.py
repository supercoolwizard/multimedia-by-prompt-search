from domain.image import Image
from application.multimedia_processor import MultimediaProcessorStrategy
from PIL import Image

class ImageProcessor(MultimediaProcessorStrategy):
    def __init__(self, describer, encoder):
        self.describer = describer
        self.encoder = encoder

    def image_preprocessor(self, image_path):
        image = Image.open(image_path).convert("RGB")
        return image

    def process(self, image_path):
        image = self.image_preprocessor(image_path)
        description = self.describer.describe(image)
        embeddings = self.encoder.encode(description)

        image_data = Image(
            text_desciription=description,
            embedding=embeddings,
            path=image_path,
        )

        return image_data
