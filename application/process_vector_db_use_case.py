class ProcessVectorDBUseCase:
    def __init__(self, vector_database):
        self.db = vector_database
        self.db.create_collection()

    def execute(self, filled_entities):
        for entity in filled_entities:
            self.db.upsert(entity)
