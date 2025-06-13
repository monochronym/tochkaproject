from pydantic_settings import BaseSettings, SettingsConfigDict
import os

# class Settings(BaseSettings):
#     DB_HOST: str
#     DB_PORT: int
#     DB_NAME: str
#     DB_USER: str
#     DB_PASSWORD: str
#     SECRET_KEY: str
#     ALGORITHM: str
#
#     model_config = SettingsConfigDict(
#         env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env")
#     )
#
#
# settings = Settings()
#
#
#
# def get_auth_data():
#     return {"secret_key": settings.SECRET_KEY, "algorithm": settings.ALGORITHM}