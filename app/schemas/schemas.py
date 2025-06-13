from pydantic import BaseModel, UUID4, Field
from datetime import datetime
from enum import Enum


#Enums
class Direction(Enum):
    BUY = 'BUY'
    SELL = 'SELL'


class OrderStatus(Enum):
    NEW = 'NEW'
    EXECUTED = 'EXECUTED'
    PARTIALLY_EXECUTED = 'PARTIALLY_EXECUTED'
    CANCELLED = 'CANCELLED'


class UserRole(Enum):
    USER = 'USER'
    ADMIN = 'ADMIN'


#Schemas

class body_deposit_api_v1_admin_balance_deposit_post(BaseModel):
    user_id: UUID4 = Field(title='User Id', examples=["35b0884d-9a1d-47b0-91c7-eecf0ca56bc8"])
    ticker: str = Field(title="Ticker", examples=["MEMCOIN"])
    amount: int = Field(title="Amount", ge=0)


class body_withdraw_api_v1_admin_balance_withdraw_post(BaseModel):
    user_id: UUID4 = Field(title='User Id', examples=["35b0884d-9a1d-47b0-91c7-eecf0ca56bc8"])
    ticker: str = Field(title="Ticker", examples=["MEMCOIN"])
    amount: int = Field(title="Amount", ge=0)


class createOrderResponse(BaseModel):
    success: bool = Field(title="Success", default=True)
    order_id: UUID4 = Field(title="Order Id")


class instrument(BaseModel):
    name: str = Field(title="Name")
    ticker: str = Field(title="Ticker", pattern="^[A-Z]{2,10}$")


class level(BaseModel):
    price: int = Field(title="Price")
    qty: int = Field(title="Qty")


class l2Orderbook(BaseModel):
    bid_levels: list[level] = Field(title='Bid levels')
    ask_levels: list[level] = Field(title='Ask levels')


class limitOrderBody(BaseModel):
    direction: Direction
    ticker: str = Field(title="Ticker")
    qty: int = Field(title="Qty", ge=1)
    price: int = Field(title="Price", gt=0)


class limitOrder(BaseModel):
    id: UUID4 = Field(title='Id')
    status: OrderStatus
    user_id: UUID4 = Field(title='User Id')
    timestamp: datetime = Field(title='Timestamp')
    body: limitOrderBody
    filled: int = Field(title="Filled", default=0)


class marketOrderBody(BaseModel):
    direction: Direction
    ticker: str = Field(title="Ticker")
    qty: int = Field(title="Qty", ge=1)


class marketOrder(BaseModel):
    id: UUID4 = Field(title='Id')
    status: OrderStatus
    user_id: UUID4 = Field(title='User Id')
    timestamp: datetime = Field(title='Timestamp')
    body: marketOrderBody


class transaction(BaseModel):
    ticker: str = Field(title='Ticker')
    amount: int = Field(title='Amount')
    price: int = Field(title='Price')
    timestamp: datetime = Field(title='Timestamp')


class user(BaseModel):
    id: UUID4 = Field(title='Id')
    name: str = Field(min_length=3, title='Name')
    role: UserRole
    api_key: str = Field(title='Api key')


class newUser(BaseModel):
    name: str = Field(min_length=3)


class ok(BaseModel):
    success: bool = Field(default=True, title='Success')
