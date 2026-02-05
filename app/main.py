from fastapi import FastAPI
from app.api.products import router as product_router

app = FastAPI(title="Price Tracker")
app.include_router(product_router)
