import decimal
import uuid
from pydantic import BaseModel, AnyHttpUrl, Field

from app.domain.enums import Status


class Product(BaseModel):
    id: uuid.UUID = Field(default=uuid.uuid4)
    name: str
    user_id: uuid.UUID
    url: AnyHttpUrl
    current_price: decimal.Decimal = Field(max_digits=10, decimal_places=2)
    target_price: decimal.Decimal = Field(max_digits=10, decimal_places=2)
    status: Status = Status.ACTIVE

    class Config:
        from_attributes = True



