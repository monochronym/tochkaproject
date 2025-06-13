from app.dao.base import BaseDAO
from app.schemas.models import Transaction


class TransactionDAO(BaseDAO):
    model = Transaction