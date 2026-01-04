from datetime import datetime, timezone

from sqlalchemy.exc import SQLAlchemyError
from typing_extensions import override

from flaskr.core.base.repository import BaseRepository
from flaskr.core.extensions import db
from flaskr.domains.tables.models import Table, TableStatus


class TableRepository(BaseRepository):
    model = Table

    @override
    def update(self, item_id: int, data: TableStatus) -> bool:
        entity = db.session.get(self.model, item_id)
        entity.status = data
        entity.last_updated = datetime.now(timezone.utc)
        try:
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            print(e)
            return False
