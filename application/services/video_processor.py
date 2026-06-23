from domain.frame import Frame
from application.services.multimedia_processor import MultimediaProcessorStrategy


class VideoProcessor(MultimediaProcessorStrategy):
    def __init__(self, slicer, describer, encoder, video_to_image_service):
        self.slicer = slicer
        self.describer = describer
        self.encoder = encoder
        self.vtis = video_to_image_service

    def process(self, video_path):
        timestamps = self.slicer.slice(video_path)

        # frames = []

        for timestamp in timestamps:
            frame = self.vtis.video_frame_to_array_ffmpeg(video_path, timestamp)

            description = self.describer.describe(frame)
            vector = self.encoder.encode(description)

            frame_data = Frame(
                text_description=description,
                vector=vector,
                path=video_path,
                timestamp=timestamp,
            )
            return frame_data

            # frames.append(frame_data)

        # return frames

