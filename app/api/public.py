from app.api.auth import auth
from typing import Annotated
from fastapi import APIRouter, Depends, Header
from app.dao.instruments import InstrumentDAO
from app.dao.transactions import TransactionDAO
from app.schemas.schemas import instrument, transaction, l2Orderbook
from app.api.token import auth_dependency, token_auth
router = APIRouter(prefix="/public")

router.include_router(auth)

@router.get("/instrument")
async def get_list_instruments(authorization: Annotated[str | None, Header()]) -> list[instrument]:
    return await InstrumentDAO.find_all()

@router.get("/transactions/{ticker}")
async def get_transaction_history(ticker:str) -> list[transaction]:
    return await TransactionDAO.find_by_filter(ticker=ticker)

@router.get("/orderbook/{ticker}")
async def get_orderbook(ticker:str) -> l2Orderbook:
    return await TransactionDAO.find_by_filter(ticker=ticker)