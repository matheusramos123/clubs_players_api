from typing import List 

from fastapi import APIRouter  
from fastapi import status 
from fastapi import Depends 
from fastapi import HTTPException
from fastapi import Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


from models.times import TimesModel
from schemas.times_schema import TimesSchemas,  TimesSchemasCreate
from core.deps import get_session   

router = APIRouter()

@router.post('/times',status_code=status.HTTP_201_CREATED, response_model= TimesSchemas)
async def post_time(time:TimesSchemasCreate, db:AsyncSession = Depends(get_session)):
    novo_time = TimesModel(nome = time.nome)
    db.add(novo_time)
    await db.commit()
    await db.refresh(novo_time)
    return novo_time

@router.get('/times',response_model=List[TimesSchemas])
async def get_times(db: AsyncSession = Depends(get_session)):
        query = select(TimesModel)
        result = await db.execute(query)
        times: List[TimesModel] = result.scalars().all()

        return times

@router.get('/times/{time_id}', response_model=TimesSchemas, status_code=status.HTTP_200_OK)
async def get_time(time_id: int, db: AsyncSession = Depends(get_session)):
    query = select(TimesModel).filter(TimesModel.id == time_id)
    result = await db.execute(query)
    time = result.scalar_one_or_none()
    if time:
         return time
    else:
         raise HTTPException(detail='ID do time não encontrado...', status_code= status.HTTP_404_NOT_FOUND)
    
@router.put('/times/{time_id}',response_model= TimesSchemas, status_code=status.HTTP_202_ACCEPTED)
async def put_time(time_id: int, time: TimesSchemasCreate ,db: AsyncSession = Depends(get_session)):
    query = select(TimesModel).filter(TimesModel.id == time_id)
    result = await db.execute(query)
    time_up = result.scalar_one_or_none()

    if time_up:

        time_up.nome = time.nome

        await db.commit()
        await db.refresh(time_up)

        return time_up 
    else:
        raise  HTTPException(detail='ID do time não encontrado...',status_code=status.HTTP_404_NOT_FOUND)
    
@router.delete('/times/{time_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_time(time_id: int, db: AsyncSession = Depends(get_session)):
    query = select(TimesModel).filter(TimesModel.id == time_id)
    result = await db.execute(query) 
    time_del = result.scalar_one_or_none()

    if not time_del:
        raise HTTPException(detail='ID do time não encontrado...',status_code=status.HTTP_404_NOT_FOUND)
    
    await db.delete(time_del)
    await db.commit()

    return None
         
    

