from datetime import datetime, timezone
from typing import TYPE_CHECKING, Dict, List

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from flaskr.core.base.model import BaseModel

if TYPE_CHECKING:
    from flaskr.domains.product.models import Product

"""
if TYPE_CHECKING:
    from flaskr.domains.product import Product
"""


class Category(BaseModel):
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=lambda: datetime.now(timezone.utc)
    )

    products: Mapped[List["Product"]] = relationship(back_populates="category")

    @property
    def serialize(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at.isoformat(),
        }
