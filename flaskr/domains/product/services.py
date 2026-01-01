from typing import Any, Dict

from flask import abort

from flaskr.core.base.services import BaseService
from flaskr.domains.product.models import Product
from flaskr.domains.product.repositories import ProductRepository


class ProductService(BaseService):
    repository: ProductRepository
    repository = ProductRepository()

    def get_by_id(self, item_id: int) -> Any | None:
        product = self.repository.get_by_id(item_id)

        if product is None:
            abort(404, description="Product not found")

        response = product.serialize
        response["category"] = {
            "id": product.category.id,
            "name": product.category.name,
        }
        return response

    def create_new_product(
        self,
        name: str = None,
        price: float = None,
        stock: int = None,
        category_id: int = None,
    ) -> Dict | None:
        return self.create_new_item(
            model_class=Product,
            func_name="get_by_name",
            unique_key=name,
            price=price,
            stock=stock,
            name=name,
            category_id=category_id,
        )
