from app.dao.base import BaseDAO
from app.schemas.models import User


class UserDAO(BaseDAO):
    model = User