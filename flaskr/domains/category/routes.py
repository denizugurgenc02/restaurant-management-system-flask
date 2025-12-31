from flask import request

from flaskr.core.base.routes import BaseRoutes
from flaskr.domains.category import bp
from flaskr.domains.category.services import CategoryService


class CategoryListAPI(BaseRoutes):
    service = CategoryService()

    def get(self):
        category_data = self.service.list_items()
        return self.format_response(data=category_data)

    def post(self):
        data = request.get_json()
        new_category = self.service.create_new_category(name=data.get("name"))

        response = self.format_response(data=new_category)
        return response, 201


class CategoryDetailsAPI(BaseRoutes):
    service = CategoryService()

    def get(self, category_id: int):
        category = self.service.get_by_id(category_id)
        return self.format_response(data=category)

    def patch(self, category_id: int):
        data = request.get_json()
        response = self.service.update_item(item_id=category_id, data=data)
        return self.format_response(data=response)

    def delete(self, category_id: int):
        response = self.service.delete_item(item_id=category_id)
        return self.format_response({"deletion": response})


bp.add_url_rule(
    "/", view_func=CategoryListAPI.as_view("category_list_api"), methods=["GET", "POST"]
)

bp.add_url_rule(
    "/<int:category_id>/",
    view_func=CategoryDetailsAPI.as_view("category_details_api"),
    methods=["GET", "PATCH", "DELETE"],
)
