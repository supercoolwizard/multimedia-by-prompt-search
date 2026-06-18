from pathlib import Path
from services.fastvlm.app import FastVLMDescriber
from settings import TARGET_DIR
from infrastructure.multimedia_type_detector import MultimediaTypeFinder
from infrastructure.video_to_image_by_timestamp import VideoToImageService
from application.image_processor import ImageProcessor
from application.video_processor import VideoProcessor




mtf = MultimediaTypeFinder()
describer = FastVLMDescriber()
encoder = Encoder()
tokenizer = Tokenizer("BAAI/bge-large-en-v1.5")
slicer = VideoSlicer()
vtis = VideoToImageService()

image_processor = ImageProcessor(describer, tokenizer, encoder)
video_processor = VideoProcessor(slicer, describer, tokenizer, vtis)

dispatcher = MultimediaDispatcher(image_processor, video_processor)

runner = ProcessDirectoryUseCase(mtf, dispatcher, TARGET_DIR)
results = runner.execute()

for r in results:
    print(r)
