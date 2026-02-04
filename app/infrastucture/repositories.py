from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.models import Product
from app.infrastucture.models import ProductTable


class ProductRepository:
    def __init__(self,session: AsyncSession):
        self.session = session

    async def add_product(self, product: Product) -> Product:
        new_product = ProductTable(
            id=product.id,
            user_id=product.user_id,
            name=product.name,
            url=str(product.url),
            current_price=product.current_price,
            target_price=product.target_price,
            status=product.status
        )

        self.session.add(new_product)
        await self.session.commit()
        await self.session.refresh(new_product)
        return product

