from abc import ABC, abstractmethod

class OutputProcessor(ABC):
    @abstractmethod
    def create_dict_of_rows(self, results):
        pass

    @abstractmethod
    def list_of_paths_maker(self, results):
        pass
