import uuid

class ProductEntity:
    def __init__(self, name: str, description: str, quantity: int):
        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.quantity = quantity