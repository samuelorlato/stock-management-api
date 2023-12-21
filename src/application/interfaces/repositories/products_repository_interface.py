from abc import ABC, abstractmethod
import typing
from src.domain.product_entity import ProductEntity

class ProductsRepositoryInterface(ABC):
    @abstractmethod
    def create_product(self, product_entity: ProductEntity) -> None:
        """Create a new product"""

    @abstractmethod
    def update_product(self, id: str, name: str, description: str, quantity: int) -> None:
        """Update a product"""

    @abstractmethod
    def delete_product(self, id: str) -> None:
        """Delete a product"""

    @abstractmethod
    def get_product(self, id: str) -> ProductEntity:
        """Get a product"""

    @abstractmethod
    def get_products(self) -> typing.List[ProductEntity]:
        """Get all products"""