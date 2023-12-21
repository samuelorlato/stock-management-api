from flask import Flask

from injector import inject, singleton, Module, Binder

from src.adapters.api.products.products_controller import urls_blueprint
from src.adapters.api.products.products_mapper import ProductsPresenterMapper
from src.adapters.spi.db.firestore_db.firestore_products_repository import FirestoreProductsRepository
from src.adapters.spi.db.firestore_db.firestore_db_connection import FirestoreDbConnection

from src.application.interfaces.mappers.api_mapper_interface import ApiMapperInterface
from src.application.interfaces.repositories.products_repository_interface import ProductsRepositoryInterface
from src.application.interfaces.spi.db_interface import DbInterface

class AppModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(ApiMapperInterface, to=ProductsPresenterMapper, scope=singleton)
        binder.bind(ProductsRepositoryInterface, to=FirestoreProductsRepository, scope=singleton)
        binder.bind(DbInterface, to=FirestoreDbConnection, scope=singleton)

def create_app() -> Flask:
    app: Flask = Flask(__name__)
    app.config["INJECTOR_MODULES"] = [AppModule]
    app.register_blueprint(urls_blueprint)

    return app