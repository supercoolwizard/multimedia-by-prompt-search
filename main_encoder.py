from pathlib import Path
from application.multimedia_dispatcher import MultimediaDispatcher
from infrastructure.video_slicer import VideoSlicer
from services.bge_small_encoder import BGEEncoder
from services.fastvlm_image_describer import FastVLMImageDescriber
from settings import TARGET_DIR
from infrastructure.multimedia_type_detector import MultimediaTypeFinder
from infrastructure.video_to_image_by_timestamp import VideoToImageService
from application.image_processor import ImageProcessor
from application.video_processor import VideoProcessor
from application.process_directory_use_case import ProcessDirectoryUseCase

mtf = MultimediaTypeFinder()
describer = FastVLMImageDescriber()
encoder = BGEEncoder()
slicer = VideoSlicer()
vtis = VideoToImageService()

image_processor = ImageProcessor(describer, encoder)
video_processor = VideoProcessor(slicer, describer, vtis)

dispatcher = MultimediaDispatcher(image_processor, video_processor)
runner = ProcessDirectoryUseCase(mtf, dispatcher, TARGET_DIR)
results = runner.execute()
for r in results:
    print(r)
