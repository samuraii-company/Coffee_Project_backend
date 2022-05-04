from fastapi import FastAPI
from restapi.users import routers as users_router
from restapi.auth import router as auth_router
from restapi.orders import routers as orders_router
from restapi.coffee import routers as coffee_router

app = FastAPI(title="EcommerceAPI", version="0.1.0")

app.include_router(auth_router.router)
app.include_router(users_router.router)
app.include_router(orders_router.router)
app.include_router(coffee_router.router)


@app.get("/")
async def root():
    return {"message": "Coffee Rest API"}