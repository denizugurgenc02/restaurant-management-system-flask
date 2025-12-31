from typing import Dict

from flaskr.core.base.services import BaseService
from flaskr.domains.category.models import Category
from flaskr.domains.category.repositories import CategoryRepository


class CategoryService(BaseService):
    repository = CategoryRepository()

    def create_new_category(self, name: str) -> Dict | None:
        return self.create_new_item(
            model_class=Category, func_name="get_by_name", unique_key=name, name=name
        )
