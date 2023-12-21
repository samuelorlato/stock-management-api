from src.application.interfaces.usecases.create_product_usecase_interface import CreateProductUsecase
from src.application.interfaces.repositories.products_repository_interface import ProductsRepositoryInterface

from src.domain.product_entity import ProductEntity
from src.domain.errors.errors import InternalError

class CreateProductUsecase(CreateProductUsecase):
    def __init__(self, repository: ProductsRepositoryInterface) -> None:
        self.repository = repository

    def execute(self, product_entity: ProductEntity) -> None:
        try:
            self.repository.create_product(product_entity)

        except Exception as exception:
            raise InternalError("Repository error", original_exception=exception)