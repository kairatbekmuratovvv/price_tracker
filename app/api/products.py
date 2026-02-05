from fastapi import APIRouter, FastAPI, status
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.models import Product
from app.infrastucture.database import get_db
from app.infrastucture.repositories import ProductRepository

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=Product)
async def create_product(
        product_data:Product,
        db: AsyncSession = Depends(get_db)
):
    repository = ProductRepository(db)
    created_product = await repository.add_product(product_data)
    return created_product