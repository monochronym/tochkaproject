from fastapi import APIRouter
from app.schemas.schemas import user, marketOrderBody, marketOrder, ok
from app.api.public import router
from app.api.admin import admin
from app.api.balance import api_balance
apirouter = APIRouter(prefix="/api/v1")
apirouter.include_router(router)
apirouter.include_router(admin)
apirouter.include_router(api_balance)

@apirouter.get("/getsomething")
async def get_something(user: user):
    return "qwe"

@apirouter.get("/getsomething2")
async def get_something(marketorder:marketOrderBody):
    return "qwe"

@apirouter.get("/getsomething3")
async def get_something(marketorder:marketOrder):
    return "qwe"