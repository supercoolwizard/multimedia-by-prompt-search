from uuid import uuid5, NAMESPACE_URL

class IdGenerator:
    def generate_id(self, path):
        key = path

        return str(uuid5(NAMESPACE_URL, key))
