from app.dao.base import BaseDAO
from app.schemas.models import Ticker


class TickerDAO(BaseDAO):
    model = Ticker