from typing import ClassVar
from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'

    DBBaseModel: ClassVar[DeclarativeMeta] = declarative_base()

    class Config():
        case_sensitive = True

settings = Settings()

