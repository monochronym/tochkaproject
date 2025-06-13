from app.dao.base import BaseDAO
from app.schemas.models import Instrument


class InstrumentDAO(BaseDAO):
    model = Instrument