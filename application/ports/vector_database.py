from abc import ABC, abstractmethod

class VectorDatabase(ABC):
    @abstractmethod
    def create_collection(collection_name):
        pass

    @abstractmethod
    def upsert(record):
        pass

    @abstractmethod
    def search(query_vector, limit):
        pass
