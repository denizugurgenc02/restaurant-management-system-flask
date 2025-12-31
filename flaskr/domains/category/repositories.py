from typing import Optional

from sqlalchemy import select

from flaskr.core.base.repository import BaseRepository, db
from flaskr.domains.category.models import Category


class CategoryRepository(BaseRepository[Category]):
    model = Category

    def get_by_name(self, name: str) -> Optional[Category]:
        query = select(self.model).filter_by(name=name)
        return db.session.execute(query).scalar_one_or_none()
