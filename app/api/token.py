from fastapi import Request, HTTPException, status, Header
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials, OAuth2AuthorizationCodeBearer
from typing import Annotated

class TokenAuthScheme(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials:
        credentials: HTTPAuthorizationCredentials = await super(TokenAuthScheme).__call__(request)

        if credentials.scheme.lower() != "token":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authorization scheme. Expected 'Token'.",
            )
        return credentials

async def verify_token(authorization: Annotated[str | None, Header()]):
    if not authorization.startswith("TOKEN "):
        raise HTTPException(status_code=401, detail="Invalid token format")
    token = authorization.split(" ")[1]
    # Add your token validation logic here
    return token

from fastapi import FastAPI, Depends

app = FastAPI(dependencies=[Depends()])

token_auth = TokenAuthScheme()

async def auth_dependency(credentials: HTTPAuthorizationCredentials = Depends(token_auth)):
    token = credentials.credentials
    print(f"Token получен: {token}")
    # Добавь здесь валидацию токена, если нужно
    return token

# @app.get("/protected")
# async def protected_route(token=Depends(auth_dependency)):
#     return {"message": "Доступ разрешен", "token": token}