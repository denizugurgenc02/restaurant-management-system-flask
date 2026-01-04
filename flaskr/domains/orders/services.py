from typing import Any, Dict

from flask import abort

from flaskr.core.base.services import BaseService
from flaskr.domains.orders.models import Order
from flaskr.domains.orders.repository import OrderRepository


class OrderService(BaseService):
    repository: OrderRepository
    repository = OrderRepository()

    def get_by_id(self, item_id: int) -> Any | None:
        order = self.repository.get_by_id(item_id=item_id)

        if order is None:
            abort(404, description="Order not found")

        response = order.serialize
        response["user"] = {
            "id": order.user.id,
            "username": order.user.username,
            "email": order.user.email,
            "created_at": order.created_at,
            "display_name": order.user.display_name,
        }
        return response

    def create_new_order(self, user_id: int):
        order = Order(
            user_id=user_id,
        )
        return self.repository.add(order)

    def update_order_products(self, item_id: int, data: Dict) -> Dict | None:
        abort(500, description="this endpoint is not available")

    def delete_order_products(self):
        abort(500, description="this endpoint is not available")
