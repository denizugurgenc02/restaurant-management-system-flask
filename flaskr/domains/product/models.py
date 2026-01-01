from datetime import datetime, timezone
from typing import TYPE_CHECKING, Dict

from sqlalchemy import DateTime, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from flaskr.core.base.model import BaseModel, mapped_foreign_key

if TYPE_CHECKING:
    from flaskr.domains.category.models import Category


class Product(BaseModel):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=lambda: datetime.now(timezone.utc)
    )
    price: Mapped[float] = mapped_column(Float, default=0)
    stock: Mapped[int] = mapped_column(Integer, default=0)

    category_id: Mapped[int] = mapped_foreign_key("category.id")
    category: Mapped["Category"] = relationship(back_populates="products")

    @property
    def serialize(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at.isoformat(),
            "price": self.price,
            "stock": self.stock,
        }
