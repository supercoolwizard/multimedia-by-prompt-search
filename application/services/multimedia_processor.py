from abc import ABC, abstractmethod

class MultimediaProcessorStrategy(ABC):
    @abstractmethod
    def process(self, multimedia_path, id_generator):
        pass
