from typing import Any
from src.application.interfaces.mappers.api_mapper_interface import ApiMapperInterface
from src.adapters.api.products.products_presenter import ProductsPresenter
from src.domain.product_entity import ProductEntity
from src.domain.errors.errors import ValidationError
from jsonschema import validate

class ProductsPresenterMapper(ApiMapperInterface):
    def to_api(self, entity: ProductEntity) -> ProductsPresenter:
        return ProductsPresenter(entity.fact_txt, entity.fact_length)

    def to_entity(self, payload: Any) -> ProductEntity:
        schema = {
            "title": "Product",
            "type": "object",
            "required": ["name"],
            "properties": {
                "name": {
                    "type": "string"
                },
                "description": {
                    "type": "string"
                },
                "quantity": {
                    "type": "integer",
                    "minimum": 0
                }
            }
        }

        try:
            validate(payload, schema)

            name = payload["name"]
            description = payload.get("description", "")
            quantity = payload.get("quantity", 0)

            product = ProductEntity(name, description, quantity)
            
            return product

        except Exception as exception:
            raise ValidationError("Invalid payload", original_exception=exception)