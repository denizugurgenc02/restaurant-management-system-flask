from datetime import datetime, timezone
from typing import TYPE_CHECKING, Dict

from sqlalchemy import DateTime, Integer
from sqlalchemy.orm import Mapped, relationship

from flaskr.core.base.model import BaseModel, mapped_column, mapped_foreign_key

if TYPE_CHECKING:
    from flaskr.domains.user.models import User


class Order(BaseModel):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=lambda: datetime.now(timezone.utc)
    )

    user_id: Mapped[int] = mapped_foreign_key("users.id")
    user: Mapped["User"] = relationship(back_populates="orders")

    @property
    def serialize(self) -> Dict:
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
        }
