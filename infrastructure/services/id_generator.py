from uuid import uuid5, NAMESPACE_URL

class IdGenerator:
    def generate_id(self, description):
        key = description
        return str(uuid5(NAMESPACE_URL, key))
