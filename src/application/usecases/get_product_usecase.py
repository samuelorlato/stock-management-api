from src.application.interfaces.usecases.get_product_usecase_interface import GetProductUsecase
from src.application.interfaces.repositories.products_repository_interface import ProductsRepositoryInterface

from src.domain.product_entity import ProductEntity
from src.domain.errors.errors import InternalError

class GetProductUsecase(GetProductUsecase):
    def __init__(self, repository: ProductsRepositoryInterface) -> None:
        self.repository = repository

    def execute(self, id: str) -> ProductEntity:
        try:
            product: ProductEntity = self.repository.get_product(id)
            return product

        except Exception as exception:
            raise InternalError("Repository error", original_exception=exception)