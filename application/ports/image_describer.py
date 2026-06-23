from abc import ABC, abstractmethod

class ImageDescriber(ABC):
    @abstractmethod
    def describe(self, image):
        pass
