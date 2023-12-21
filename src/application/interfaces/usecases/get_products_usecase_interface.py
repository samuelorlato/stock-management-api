from abc import ABC, abstractmethod
from src.domain.product_entity import ProductEntity
from src.application.interfaces.repositories.products_repository_interface import ProductsRepositoryInterface

class GetProductsUsecase(ABC):
    def __init__(self, repository: ProductsRepositoryInterface):
        self.repository = repository
        
    @abstractmethod
    def execute(self) -> typing.List[ProductEntity]:
        """Execute GetProductsUsecase, getting all registered products"""