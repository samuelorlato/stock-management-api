from abc import ABC, abstractmethod
from src.domain.product_entity import ProductEntity
from src.application.interfaces.repositories.products_repository_interface import ProductsRepositoryInterface

class DeleteProductUsecase(ABC):
    def __init__(self, repository: ProductsRepositoryInterface):
        self.repository = repository
        
    @abstractmethod
    def execute(self, id: str) -> None:
        """Execute DeleteProductUsecase, deleting the product with the received id"""