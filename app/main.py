from fastapi import FastAPI
from app.api.products import router as product_router
from app.infrastucture.database import engine, Base

app = FastAPI(title="Price Tracker")
app.include_router(product_router)


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
