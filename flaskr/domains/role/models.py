from typing import TYPE_CHECKING, Dict, List

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from flaskr.core.extensions import BaseModel

if TYPE_CHECKING:
    from flaskr.domains.user.models import User


class Role(BaseModel):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(30), unique=True)

    users: Mapped[List["User"]] = relationship(back_populates="role")

    @property
    def serialize(self) -> Dict:
        return {"id": self.id, "name": self.name}
