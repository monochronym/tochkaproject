from app.dao.balance import BalanceDAO

from fastapi import APIRouter, Header, HTTPException, Depends
from app.dao.user import UserDAO
from app.dao.instruments import InstrumentDAO
from app.dao.ticker import TickerDAO
from typing import Annotated
from app.api.token import verify_token
from uuid import UUID
from app.schemas.schemas import body_deposit_api_v1_admin_balance_deposit_post, ok, instrument
admin = APIRouter(prefix="/admin")
# admin_token = key-b2b11fae-e2a5-4274-bd10-4ef170eb4b52
@admin.post("/balance/deposit", dependencies=[Depends(verify_token)])
async def deposit(authorization: Annotated[str | None, Header()], deposit_body: body_deposit_api_v1_admin_balance_deposit_post):
    if await UserDAO.find_by_filter(api_key=authorization.split(" ")[1], user_role="ADMIN") is None:
        return HTTPException(status_code=401,
                            detail="Not admin",
                            headers={"Authorization": authorization})
    user_balance = await BalanceDAO.find_by_filter(user_id=deposit_body.user_id, ticker=deposit_body.ticker)
    if user_balance is None:
        await BalanceDAO.add(**deposit_body.dict())
        return ok()
    await BalanceDAO.update(filter_by={"user_id":deposit_body.user_id}, amount=user_balance.amount+deposit_body.amount)
    return ok()

@admin.post("/balance/withdraw", dependencies=[Depends(verify_token)])
async def withdraw(authorization: Annotated[str | None, Header()], deposit_body: body_deposit_api_v1_admin_balance_deposit_post):
    if await UserDAO.find_by_filter(api_key=authorization.split(" ")[1], user_role="ADMIN") is None:
        return HTTPException(status_code=401,
                            detail="Not admin",
                            headers={"Authorization": "TOKEN"})
    user_balance = await BalanceDAO.find_by_filter(user_id=deposit_body.user_id, ticker=deposit_body.ticker)
    if user_balance is None:
        return HTTPException(status_code=401,
                             detail="Not found instrument")
    await BalanceDAO.update(filter_by={"user_id":deposit_body.user_id}, amount=user_balance.amount-deposit_body.amount)
    return ok()

@admin.delete("/user/{user_id}", dependencies=[Depends(verify_token)])
async def delete_user(authorization: Annotated[str | None, Header()],user_id:UUID):
    if await UserDAO.find_by_filter(api_key=authorization.split(" ")[1], user_role="ADMIN") is None:
        return HTTPException(status_code=401,
                            detail="Not admin",
                            headers={"Authorization": "TOKEN"})
    user = await UserDAO.find_by_id(str(user_id))
    if user is None:
        return HTTPException(status_code=400,
                             detail="User not found",
                             headers={"Authorization": "TOKEN"})
    await UserDAO.delete(False,id=str(user_id))
    return user

@admin.post("/instrument", dependencies=[Depends(verify_token)])
async def add_instument(authorization: Annotated[str | None, Header()], inst: instrument):
    if await UserDAO.find_by_filter(api_key=authorization.split(" ")[1], user_role="ADMIN") is None:
        return HTTPException(status_code=401,
                            detail="Not admin",
                            headers={"Authorization": "TOKEN"})
    await TickerDAO.add(**{"ticker": inst.ticker})
    await InstrumentDAO.add(**inst.dict())
    return ok()

@admin.delete("/instrument{ticker}", dependencies=[Depends(verify_token)])
async def delete_instument(authorization: Annotated[str | None, Header()], ticker: str):
    if await UserDAO.find_by_filter(api_key=authorization.split(" ")[1], user_role="ADMIN") is None:
        return HTTPException(status_code=401,
                            detail="Not admin",
                            headers={"Authorization": "TOKEN"})
    await InstrumentDAO.delete(False, ticker=ticker)
    await TickerDAO.delete(False, ticker=ticker)
    return ok()