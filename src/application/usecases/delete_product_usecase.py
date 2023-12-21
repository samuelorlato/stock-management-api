from src.application.interfaces.usecases.delete_product_usecase_interface import DeleteProductUsecase
from src.application.interfaces.repositories.products_repository_interface import ProductsRepositoryInterface

from src.domain.errors.errors import InternalError

class DeleteProductUsecase(DeleteProductUsecase):
    def __init__(self, repository: ProductsRepositoryInterface) -> None:
        self.repository = repository

    def execute(self, id: str) -> None:
        try:
            self.repository.delete_product(id)
            
        except Exception as exception:
            raise InternalError("Repository error", original_exception=exception)