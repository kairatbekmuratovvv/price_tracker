import decimal
import uuid

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Numeric, Enum as SAEnum

from app.domain.enums import Status
from app.infrastucture.database import Base


class ProductTable(Base):
    __tablename__ = "products"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True,default=uuid.uuid4)
    user_id:Mapped[uuid.UUID] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(String(255))
    url: Mapped[str] = mapped_column(String(1024))
    current_price: Mapped[decimal.Decimal] = mapped_column(Numeric(10,2), nullable=False)
    target_price: Mapped[decimal.Decimal] = mapped_column(Numeric(10,2), nullable=False)
    status: Mapped[Status] = mapped_column(SAEnum(Status),default=Status.ACTIVE, nullable=False)
