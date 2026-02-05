from uuid import uuid4

from fastapi import APIRouter, FastAPI, status
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.models import Product, ProductCreate
from app.infrastucture.database import get_db
from app.infrastucture.repositories import ProductRepository

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=Product)
async def create_product(
        product_in:ProductCreate,
        db: AsyncSession = Depends(get_db)
):
    current_user_id = uuid4()

    repository = ProductRepository(db)
    created_product = await repository.add_product(product_in, current_user_id)
    await db.commit()
    return created_product