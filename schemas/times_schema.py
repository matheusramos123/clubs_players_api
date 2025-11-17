from pydantic import BaseModel
from typing import Optional

class TimesSchemas(BaseModel):
    id: Optional[int]
    nome: str

class TimesSchemasCreate(BaseModel):
    nome: str

    class Config():
        orm_mode = True