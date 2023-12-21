import typing

from src.application.interfaces.usecases.get_products_usecase_interface import GetProductsUsecase
from src.application.interfaces.repositories.products_repository_interface import ProductsRepositoryInterface

from src.domain.product_entity import ProductEntity
from src.domain.errors.errors import InternalError

class GetProductsUsecase(GetProductsUsecase):
    def __init__(self, repository: ProductsRepositoryInterface) -> None:
        self.repository = repository

    def execute(self) -> typing.List[ProductEntity]:
        try:
            products: typing.List[ProductEntity] = self.repository.get_products()
            return products

        except Exception as exception:
            raise InternalError("Repository error", original_exception=exception)