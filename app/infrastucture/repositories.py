from decimal import Decimal
from uuid import uuid4

from pydantic.v1 import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.enums import Status
from app.domain.models import Product, ProductCreate
from app.infrastucture.models import ProductTable


class ProductRepository:
    def __init__(self,session: AsyncSession):
        self.session = session

    async def add_product(self, product_in: ProductCreate, user_id: UUID4) -> Product:
        product_id = uuid4()
        db_product = ProductTable(
            id=product_id,
            user_id=user_id,
            name=product_in.name,
            url=str(product_in.url),
            current_price=Decimal("0.00"),
            target_price=product_in.target_price,
            status=Status.ACTIVE
        )
        self.session.add(db_product)

        return Product(
            id=product_id,
            user_id=user_id,
            current_price=Decimal("0.00"),
            **product_in.model_dump()
        )

