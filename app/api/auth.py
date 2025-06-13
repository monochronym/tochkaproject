from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta, timezone
from app.config import get_auth_data
from app.schemas.schemas import newUser, user, UserRole
from app.dao.user import UserDAO
import uuid
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# def get_password_hash(password: str) -> str:
#     return pwd_context.hash(password)
#
#
# def verify_password(plain_password: str, hashed_password: str) -> bool:
#     return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=30)
    to_encode.update({"exp": expire})
    auth_data = get_auth_data()
    encode_jwt = jwt.encode(to_encode, auth_data['secret_key'], algorithm=auth_data['algorithm'])
    return encode_jwt


from fastapi import Depends, APIRouter

auth = APIRouter()

@auth.post("/register")
async def register(user_data:newUser):
    return await UserDAO.add(
        id = uuid.uuid4(),
        name = user_data.name,
        user_role = UserRole.USER,
        api_key = "key-" + str(uuid.uuid4()))