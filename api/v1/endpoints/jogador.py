from typing import List 

from fastapi import APIRouter  
from fastapi import status 
from fastapi import Depends 
from fastapi import HTTPException
from fastapi import Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.jogadores import JogadorModel
from schemas.jogadores_schema import JogadorSchema, JogadorSchemaCreate
from core.deps import get_session   

router = APIRouter()

@router.post('/jogador',status_code=status.HTTP_201_CREATED, response_model= JogadorSchema)
async def post_jogador(jogador:JogadorSchemaCreate, db:AsyncSession = Depends(get_session)):
    novo_jogador = JogadorModel(
         nome = jogador.nome,
         posicao = jogador.posicao,
         time_id = jogador.time_id
                                )
    db.add(novo_jogador)
    await db.commit()
    await db.refresh(novo_jogador)
    return novo_jogador

@router.get('/jogador',response_model=List[JogadorSchema])
async def get_jogadores(db: AsyncSession = Depends(get_session)):
        query = select(JogadorModel)
        result = await db.execute(query)
        jogadores: List[JogadorModel] = result.scalars().all()

        return jogadores

@router.get('/jogador/{jogador_id}', response_model=JogadorSchema, status_code=status.HTTP_200_OK)
async def get_jogador(jogador_id: int, db: AsyncSession = Depends(get_session)):
    query = select(JogadorModel).filter(JogadorModel.id == jogador_id)
    result = await db.execute(query)
    jogador = result.scalar_one_or_none()
    if jogador:
         return jogador
    else:
         raise HTTPException(detail='ID do jogador não encontrado...', status_code= status.HTTP_404_NOT_FOUND)
    
@router.put('/jogador/{jogador_id}',response_model= JogadorSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_jogador(jogador_id: int, jogador: JogadorSchemaCreate ,db: AsyncSession = Depends(get_session)):
    query = select(JogadorModel).filter(JogadorModel.id == jogador_id)
    result = await db.execute(query)
    jogador_up = result.scalar_one_or_none()

    if jogador_up:

        jogador_up.nome = jogador.nome

        await db.commit()
        await db.refresh(jogador_up)

        return jogador_up 
    else:
        raise  HTTPException(detail='ID do jogador não encontrado...',status_code=status.HTTP_404_NOT_FOUND)
    
@router.delete('/jogador/{jogador_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_jogador(jogador_id: int, db: AsyncSession = Depends(get_session)):
    query = select(JogadorModel).filter(JogadorModel.id == jogador_id)
    result = await db.execute(query) 
    jogador_del = result.scalar_one_or_none()

    if not jogador_del:
        raise HTTPException(detail='ID do jogador não encontrado...',status_code=status.HTTP_404_NOT_FOUND)
    
    await db.delete(jogador_del)
    await db.commit()

    return None
       





