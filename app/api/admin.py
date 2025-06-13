from app.dao.balance import BalanceDAO

from fastapi import APIRouter, Header
from typing import Annotated
from app.api.token import token_auth

from app.schemas.schemas import body_deposit_api_v1_admin_balance_deposit_post, ok
admin = APIRouter(prefix="/admin")
# admin_token = b2b11fae-e2a5-4274-bd10-4ef170eb4b52
@admin.post("/balance/deposit")
async def deposit(deposit_body: body_deposit_api_v1_admin_balance_deposit_post, authorization: Annotated[str | None, Header()]):
    user_balance = await BalanceDAO.find_by_filter(user_id=deposit_body.user_id, ticker=deposit_body.ticker)
    if user_balance is None:
        await BalanceDAO.add(**deposit_body.dict())
        return ok()
