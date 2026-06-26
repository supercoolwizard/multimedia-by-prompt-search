from cli.platform_file_revealer import PlatformFileRevealer
from cli.table_maker import TableMaker
from infrastructure.services.multimedia_type_detector import MultimediaTypeFinder
from infrastructure.bge_small_encoder import BGEEncoder
from infrastructure.qdrant.qdrant_vdb import QdrantVectorDatabase
from infrastructure.qdrant.qdrant_output_processor import QdrantOutputProcessor
from infrastructure.ml.device import get_device_config
from cli.cli_decoder import CLIDecoder
from settings import *

from dotenv import load_dotenv
import os


load_dotenv("config.env")
hf_token = os.getenv("HF_TOKEN")
config = get_device_config()

encoder = BGEEncoder(hf_token, config)
db = QdrantVectorDatabase()
mtf = MultimediaTypeFinder()

output_processor = QdrantOutputProcessor()
table_maker = TableMaker()
revealer = PlatformFileRevealer()

cli = CLIDecoder(
    SEARCH_SCOPE,
    encoder,
    db,
    mtf,
    output_processor,
    table_maker,
    revealer,
)

cli.execute()
