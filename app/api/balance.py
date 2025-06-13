from app.dao.balance import BalanceDAO
from typing import Annotated
from fastapi import APIRouter, Header, HTTPException, Depends
from app.schemas.schemas import ok
from app.dao.user import UserDAO
from app.api.token import verify_token

api_balance = APIRouter(prefix="/balance")

@api_balance.get("/", dependencies=[Depends(verify_token)])
async def balance(authorization: Annotated[str | None, Header()]):
    user = await UserDAO.find_by_filter(api_key=authorization.split(" ")[1])
    if user is None:
        return HTTPException(status_code=401,
                            detail="Not authenticated",
                            headers={"Authorization": "TOKEN"})

    balances = await BalanceDAO.find_all(user_id=user.id)
    res = dict()
    for balance in balances:
        res[balance.ticker] = balance.amount
    return res