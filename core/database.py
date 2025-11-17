from dotenv import load_dotenv  
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import AsyncSession

from core.configs import settings 

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

engine: AsyncEngine = create_async_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autoflush= False,
    expire_on_commit= False,
    class_= AsyncSession,
    bind= engine
    )
