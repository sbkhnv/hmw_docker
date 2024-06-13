from fastapi import FastAPI,security,HTTPException
from database import session,ENGINE
from order_rouyer import order_router
from product_router import product_router
session = session(bind=ENGINE)


app = FastAPI()
app.include_router(order_router)
app.include_router(product_router)

app.get("/")
async def landing():
    return {
        "message": "Hello World"
    }
