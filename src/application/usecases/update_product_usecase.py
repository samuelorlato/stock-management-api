import typing

from src.application.interfaces.usecases.update_product_usecase_interface import UpdateProductUsecase
from src.application.interfaces.repositories.products_repository_interface import ProductsRepositoryInterface

from src.domain.product_entity import ProductEntity
from src.domain.errors.errors import InternalError

class UpdateProductUsecase(UpdateProductUsecase):
    def __init__(self, repository: ProductsRepositoryInterface) -> None:
        self.repository = repository

    def execute(self, id: str, name: str, description: str, quantity: int) -> None:
        try:
            self.repository.update_product(id, name, description, quantity)

        except Exception as exception:
            raise InternalError("Repository error", original_exception=exception)