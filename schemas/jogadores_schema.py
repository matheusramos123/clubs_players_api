from pydantic import BaseModel
from typing import Optional

class JogadorSchema(BaseModel):
    id: Optional[int]
    nome: str
    posicao: str
    time_id: int

class JogadorSchemaCreate(BaseModel):
    nome: str
    posicao: str
    time_id: int

    class Config():
        orm_mode = True