from flask import Blueprint
from flask import request

from injector import inject

from src.application.interfaces.mappers.api_mapper_interface import ApiMapperInterface
from src.application.interfaces.repositories.products_repository_interface import ProductsRepositoryInterface
from src.application.interfaces.usecases.create_product_usecase_interface import CreateProductUsecase

from src.application.usecases.create_product_usecase import CreateProductUsecase

from src.domain.product_entity import ProductEntity
from src.domain.errors.errors import CustomError

from src.adapters.api.shared.api_error_handling import ApiErrorHandling

urls_blueprint = Blueprint("urls", __name__)

@urls_blueprint.route("/products", methods=["GET"])
def get_products():
    # TODO: create repository
    # TODO: create usecase
    # TODO: create presenter mapper
    # TODO: return data
    # TODO: create error handling
    return

@urls_blueprint.route("/products/<id>", methods=["GET"])
def get_product():
    # TODO: create repository
    # TODO: create usecase
    # TODO: create presenter mapper
    # TODO: return data
    # TODO: create error handling
    return
  
@urls_blueprint.route("/products/<id>", methods=["DELETE"])
def delete_product():
    # TODO: create repository
    # TODO: create presenter mapper
    # TODO: create usecase
    # TODO: create error handling
    return

@urls_blueprint.route("/products/<id>", methods=["PATCH"])
def update_product():
    # TODO: create repository
    # TODO: create presenter mapper
    # TODO: create usecase
    # TODO: create error handling
    return

@urls_blueprint.route("/products", methods=["POST"])
@inject
def create_product(
    products_presenter_mapper: ApiMapperInterface,
    products_repository: ProductsRepositoryInterface
):
    data = request.get_json()

    try:
        product_entity: ProductEntity = products_presenter_mapper.to_entity(data)
        
        create_product_usecase: CreateProductUsecase = CreateProductUsecase(products_repository)
        create_product_usecase.execute(product_entity)

        return {
            "created_product_id": product.id
        }

    except CustomError as error:
        return ApiErrorHandling.handle_error(error)