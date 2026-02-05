import decimal
import uuid
from pydantic import BaseModel, AnyHttpUrl, Field

from app.domain.enums import Status


class ProductCreate(BaseModel):
    name: str = Field(..., max_length=255, min_length=1)
    url: AnyHttpUrl
    target_price: decimal.Decimal = Field(max_digits=10, decimal_places=2)

class Product(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    current_price: decimal.Decimal = Field(max_digits=10, decimal_places=2)
    status: Status = Status.ACTIVE

    class Config:
        from_attributes = True



