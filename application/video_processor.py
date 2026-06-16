from domain.frame import Frame

class VideoProcessor:
    def __init__(self, slicer, describer, tokenizer, video_to_image_service):
        self.slicer = slicer
        self.describer = describer
        self.tokenizer = tokenizer
        self.vtis = video_to_image_service

    def process(self, video_path):
        timestamps = self.slicer.slice(video_path)

        for timestamp in timestamps:
            frame = self.vtis.video_frame_to_array_ffmpeg(video_path, timestamp)

            description = self.describer.describe(frame)
            embeddings = self.tokenizer.tokenize(description)

            frame_data = Frame(
                text_desciription=description,
                embedding=embeddings,
                path=video_path,
                timestamp=timestamp,
            )

            return frame_data

