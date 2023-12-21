from src.application.interfaces.repositories.products_repository_interface import ProductsRepositoryInterface

from src.adapters.spi.db.firestore_db.firestore_db_connection import FirestoreDbConnection

from src.domain.product_entity import ProductEntity

import typing

class FirestoreProductsRepository(ProductsRepositoryInterface):
    def __init__(self, db_connection: FirestoreDbConnection) -> None:
        # self.mappers = ProductDbMapper()
        self.db_connection = db_connection

    def create_product(self, product_entity: ProductEntity) -> None:
        pass

    def update_product(self, id: str, name: str, description: str, quantity: int) -> None:
        pass

    def delete_product(self, id: str) -> None:
        pass    

    def get_product(self, id: str) -> ProductEntity:
        pass

    def get_products(self) -> typing.List[ProductEntity]:
        pass

