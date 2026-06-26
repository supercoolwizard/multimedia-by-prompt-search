from pathlib import Path
from dotenv import load_dotenv
import os

from application.process_vector_db_use_case import ProcessVectorDBUseCase
from infrastructure.services.id_generator import IdGenerator
from settings import TARGET_DIR

from infrastructure.ml.device import get_device_config

from application.services.multimedia_dispatcher import MultimediaDispatcher
from infrastructure.services.video_slicer import VideoSlicer
from infrastructure.bge_small_encoder import BGEEncoder
from infrastructure.fastvlm_image_describer import FastVLMImageDescriber
from infrastructure.qdrant.qdrant_vdb import QdrantVectorDatabase
from infrastructure.services.multimedia_type_detector import MultimediaTypeFinder
from infrastructure.services.video_to_image_service import VideoToImageService
from application.services.image_processor import ImageProcessor
from application.services.video_processor import VideoProcessor
from application.process_directory_use_case import ProcessDirectoryUseCase

load_dotenv("config.env")
hf_token = os.getenv("HF_TOKEN")
config = get_device_config()

type_finder = MultimediaTypeFinder()
describer = FastVLMImageDescriber(hf_token, config)
encoder = BGEEncoder(hf_token, config)
slicer = VideoSlicer()
vtis = VideoToImageService()

id_generator = IdGenerator()

image_processor = ImageProcessor(describer, encoder)
video_processor = VideoProcessor(slicer, describer, encoder, vtis)

dispatcher = MultimediaDispatcher(image_processor, video_processor)
runner = ProcessDirectoryUseCase(type_finder, dispatcher, TARGET_DIR, id_generator)

db = QdrantVectorDatabase()
db_processor = ProcessVectorDBUseCase(db)

filled_entities = runner.execute()
db_processor.execute(filled_entities)
