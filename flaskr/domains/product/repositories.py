from typing import Optional

from sqlalchemy import select

from flaskr.core.base.repository import BaseRepository, db
from flaskr.domains.product.models import Product


class ProductRepository(BaseRepository[Product]):
    model = Product

    def get_by_name(self, username: str) -> Optional[Product]:
        query = select(self.model).filter_by(name=username)
        return db.session.execute(query).scalar_one_or_none()
