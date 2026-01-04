from flask import request

from flaskr.core.base.routes import BaseRoutes
from flaskr.domains.orders.services import OrderService

from . import bp


class OrderListAPI(BaseRoutes):
    service = OrderService()

    def get(self):
        order_data = self.service.list_items()
        return self.format_response(data=order_data)

    def post(self):
        data = request.get_json()
        self.service.create_new_order(
            user_id=data.get("user_id"),
        )
        response = data
        return response, 201


class OrderDetailAPI(BaseRoutes):
    service = OrderService()

    def get(self, order_id: int):
        user = self.service.get_by_id(item_id=order_id)
        return self.format_response(data=user)

    def patch(self, order_id: int):
        data = request.get_json()

        response = self.service.update_item(item_id=order_id, data=data)
        return self.format_response(data=response)

    def delete(self, order_id: int):
        response = self.service.delete_item(item_id=order_id)
        return self.format_response({"deletion": response})


bp.add_url_rule(
    "/", view_func=OrderListAPI.as_view("order_list_api"), methods=["GET", "POST"]
)

bp.add_url_rule(
    "/<int:order_id>",
    view_func=OrderDetailAPI.as_view("order_detail_api"),
    methods=[
        "GET",
        "PATCH",
        "DELETE",
    ],
)
