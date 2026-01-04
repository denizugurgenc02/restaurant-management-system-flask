from datetime import datetime, timezone
from typing import TYPE_CHECKING, Dict

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from flaskr.core.base.model import BaseModel, mapped_foreign_key

if TYPE_CHECKING:
    from flaskr.domains.orders.models import Order
    from flaskr.domains.role.models import Role


class User(BaseModel):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(32), unique=True)
    password: Mapped[str] = mapped_column(String(128))
    display_name: Mapped[str] = mapped_column(String(16), unique=True)
    email: Mapped[str] = mapped_column(String(64), unique=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=lambda: datetime.now(timezone.utc)
    )

    role_id: Mapped[int] = mapped_foreign_key("roles.id")
    role: Mapped["Role"] = relationship(back_populates="users")

    orders: Mapped[list["Order"]] = relationship(back_populates="user")

    @property
    def serialize(self) -> Dict:
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "display_name": self.display_name,
            "email": self.email,
            "created_at": self.created_at.isoformat(),
        }
