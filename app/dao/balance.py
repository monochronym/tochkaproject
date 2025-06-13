from app.dao.base import BaseDAO
from app.schemas.models import Balance


class BalanceDAO(BaseDAO):
    model = Balance