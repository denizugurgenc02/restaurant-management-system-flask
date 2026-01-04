from typing import Dict

from typing_extensions import override

from flaskr.core.base.services import BaseService
from flaskr.domains.tables.models import Table, TableStatus
from flaskr.domains.tables.repositories import TableRepository


class TableService(BaseService):
    repository: TableRepository
    repository = TableRepository()

    @override
    def update_item(self, item_id: int, data: TableStatus) -> Dict | None:
        self.get_by_id(item_id=item_id)
        response = self.repository.update(item_id=item_id, data=data)
        if response:
            return self.get_by_id(item_id=item_id)

    def create_new_table(self):
        new_table = Table()
        return self.repository.add(new_table)
