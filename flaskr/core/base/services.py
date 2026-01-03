from typing import Any, Dict, Generic, List, Type, TypeVar

from flask import abort

T = TypeVar("T")


class BaseService(Generic[T]):
    repository: Type[T]

    def get_by_id(self, item_id: int) -> Any | None:
        item = self.repository.get_by_id(item_id=item_id)

        if item is None:
            abort(404, description="There is no item")

        response = item.serialize
        return response

    def list_items(self) -> List:
        items = self.repository.get_all()
        return [item.serialize for item in items]

    def create_new_item(
        self,
        model_class,
        stun_name: str,
        unique_key: str,
        func_name: str = "get_by_name",
        **kwargs,
    ) -> Dict | None:

        if existing_item := getattr(self.repository, func_name)(stun_name, unique_key):
            abort(
                code=409,
                description=f"this item already current."
                f" detail: {existing_item.serialize}",
            )

        new_item = self.repository.add(model_class(**kwargs))
        item_id = new_item.serialize.get("id")
        if item_id:
            return self.get_by_id(item_id=item_id)

    def update_item(self, item_id: int, data: Dict) -> Dict | None:
        self.get_by_id(item_id=item_id)
        response = self.repository.update(item_id=item_id, data=data)
        if response:
            return self.get_by_id(item_id=item_id)

    def delete_item(self, item_id: int) -> bool:
        self.get_by_id(item_id=item_id)
        return self.repository.delete(item_id=item_id)
