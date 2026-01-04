from datetime import datetime, timezone
from enum import Enum
from typing import Dict

from sqlalchemy import DateTime
from sqlalchemy import Enum as SQLEnum
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column

from flaskr.core.base.model import BaseModel


class TableStatus(Enum):
    AVAILABLE = "available"
    RESERVED = "reserved"
    OCCUPIED = "occupied"


class Table(BaseModel):
    __tablename__ = "tables"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    status: Mapped[TableStatus] = mapped_column(
        SQLEnum(TableStatus), default=TableStatus.AVAILABLE
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=lambda: datetime.now(timezone.utc)
    )
    last_updated: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    @property
    def serialize(self) -> Dict:
        return {
            "id": self.id,
            "status": (
                self.status.value if hasattr(self.status, "value") else self.status
            ),
            "created_at": self.created_at.isoformat(),
            "last_updated": (
                self.last_updated.isoformat() if self.last_updated else None
            ),
        }
