from flask import request

from flaskr.core.base.routes import BaseRoutes
from flaskr.domains.tables.models import TableStatus
from flaskr.domains.tables.services import TableService

from . import bp


class TableListAPI(BaseRoutes):
    service = TableService()

    def get(self):
        users_data = self.service.list_items()
        return self.format_response(data=users_data)

    def post(self):
        new_table = self.service.create_new_table()

        response = self.format_response(data=new_table.serialize)
        return response, 201


class TableDetailAPI(BaseRoutes):
    service = TableService()

    def get(self, table_id: int):
        table = self.service.get_by_id(item_id=table_id)
        return self.format_response(data=table)

    def patch(self, table_id: int):
        data = request.get_json()
        new_status = data.get("status")

        try:
            status_enum = TableStatus[new_status.upper()]
        except (KeyError, AttributeError) as e:
            print(e)

        response = self.service.update_item(item_id=table_id, data=status_enum)
        return self.format_response(data=response)

    def delete(self, table_id: int):
        response = self.service.delete_item(item_id=table_id)
        return self.format_response({"deletion": response})


bp.add_url_rule(
    "/", view_func=TableListAPI.as_view("table_list_api"), methods=["GET", "POST"]
)

bp.add_url_rule(
    "/<int:table_id>",
    view_func=TableDetailAPI.as_view("table_detail_api"),
    methods=["GET", "PATCH", "DELETE"],
)
