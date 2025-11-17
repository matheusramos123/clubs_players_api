from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import SessionLocal

async def get_session() -> AsyncGenerator:
   async with SessionLocal() as session:
      yield session  
