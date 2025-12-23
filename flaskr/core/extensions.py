from datetime import datetime, timezone
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar

from flask import Response, jsonify
from flask.views import MethodView
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import DeclarativeBase, mapped_column


def mapped_foreign_key(target, **kwargs):
    return mapped_column(ForeignKey(target), **kwargs)


class BaseModel(DeclarativeBase):
    pass


class BaseRoutes(MethodView):
    @staticmethod
    def format_response(data: Any, pagination: bool = False) -> Response:
        response = {
            "server_time": datetime.now(timezone.utc).isoformat(),
            "count": len(data) if isinstance(data, list) else 1,
            "items": data if isinstance(data, list) else [data],
        }

        if pagination:
            pass

        return jsonify(response)


T = TypeVar("T")


class BaseRepository(Generic[T]):
    model: Type[T]

    def get_all(self) -> List[T]:
        return list(db.session.execute(select(self.model)).scalars().all())

    def get_by_id(self, item_id: int) -> Optional[T]:
        return db.session.get(self.model, item_id)

    def update(self, item_id: int, data: Dict) -> bool:
        entity = db.session.get(self.model, item_id)

        for key, value in data.items():
            if hasattr(entity, key) and key != "id":
                setattr(entity, key, value)

        try:
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            print(e)
            return False

    def add(self, entity: T) -> T:
        db.session.add(entity)
        db.session.commit()
        return entity

    def delete(self, item_id: int) -> bool:
        entity = self.get_by_id(item_id=item_id)
        db.session.delete(entity)
        db.session.commit()

        return True


db = SQLAlchemy(model_class=BaseModel)
migrate = Migrate()
