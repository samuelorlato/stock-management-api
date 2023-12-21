from abc import ABC, abstractmethod
from src.domain.product_entity import ProductEntity
from src.application.interfaces.repositories.products_repository_interface import ProductsRepositoryInterface

class CreateProductUsecase(ABC):
    def __init__(self, repository: ProductsRepositoryInterface):
        self.repository = repository
        
    @abstractmethod
    def execute(self, product_entity: ProductEntity) -> None:
        """Execute CreateProductUsecase, creating a product using the received product_entity"""