from sqlalchemy import ForeignKey, text, Text, Enum, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base, str_uniq, uuid_pk, timestamp, str_pk
from uuid import UUID
import datetime
from app.schemas.schemas import UserRole, Direction, OrderStatus
class User(Base):
    id: Mapped[uuid_pk]
    name: Mapped[str]
    api_key: Mapped[str_uniq]
    user_role: Mapped[UserRole] = mapped_column(Enum(UserRole), nullable=False)
    balances: Mapped["Balance"] = relationship(back_populates="user")

class MarketOrder(Base):
    id: Mapped[uuid_pk]
    user_id: Mapped[UUID] = mapped_column(ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    status: Mapped[OrderStatus] = mapped_column(Enum(OrderStatus), nullable=False)
    timestamp = Mapped[timestamp]
    marketorderbody: Mapped["MarketOrderBody"] = relationship(back_populates="marketorder", uselist=False)

class MarketOrderBody(Base):
    order_id: Mapped[UUID] = mapped_column(ForeignKey("marketorders.id", ondelete="CASCADE"), primary_key=True)
    direction: Mapped[Direction] = mapped_column(Enum(Direction), nullable=False)
    ticker: Mapped[str] = mapped_column(ForeignKey("tickers.ticker", ondelete="CASCADE"), nullable=False)
    qty: Mapped[int]
    marketorder: Mapped["MarketOrder"] = relationship(back_populates="marketorderbody", uselist=False)


class LimitOrder(Base):
    id: Mapped[uuid_pk]
    user_id: Mapped[UUID] = mapped_column(ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    status: Mapped[OrderStatus] = mapped_column(Enum(OrderStatus), nullable=False)
    timestamp = Mapped[timestamp]
    limitorderbody: Mapped["LimitOrderBody"] = relationship(back_populates="limitorder", uselist=False)
    filled: Mapped[int]

class LimitOrderBody(Base):
    order_id: Mapped[UUID] = mapped_column(ForeignKey("limitorders.id", ondelete="CASCADE"), primary_key=True)
    direction: Mapped[Direction] = mapped_column(Enum(Direction), nullable=False)
    ticker: Mapped[str] = mapped_column(ForeignKey("tickers.ticker", ondelete="CASCADE"), nullable=False)
    qty: Mapped[int]
    price: Mapped[int]
    limitorder: Mapped["LimitOrder"] = relationship(back_populates="limitorderbody", uselist=False)

class Transaction(Base):
    ticker: Mapped[str] = mapped_column(ForeignKey("tickers.ticker", ondelete="CASCADE"), nullable=False)
    amount: Mapped[int]
    price: Mapped[int]
    timestamp: Mapped[datetime] = mapped_column(DateTime, primary_key=True)

class Instrument(Base):
    name: Mapped[str_pk]
    ticker: Mapped[str] = mapped_column(ForeignKey("tickers.ticker", ondelete="CASCADE"), nullable=False)

class Ticker(Base):
    ticker: Mapped[str_pk]

class Balance(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    user: Mapped["User"] = relationship(back_populates="balances")
    ticker: Mapped[str] = mapped_column(ForeignKey("tickers.ticker", ondelete="CASCADE"), nullable=False)
    amount: Mapped[int]