# booksToScrape/pipeline/oeuvre_pipeline.py
from sqlmodel import SQLModel, Field, Session, select, create_engine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession
import os
from dotenv import load_dotenv
from pathlib import Path
import asyncio

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWD = os.getenv("DATABASE_PASSWD")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE_NAME= os.getenv("DATABASE_NAME")
DATABASE_IP = os.getenv("DATABASE_IP")

DATABASE_URL = f"postgresql+asyncpg://{DATABASE_USER}:{DATABASE_PASSWD}@{DATABASE_IP}:{DATABASE_PORT}/{DATABASE_NAME}"


class DataBase():
    def __init__(self):
        # echo=False => désactive le spam SQLAlchemy
        self.engine = create_async_engine(DATABASE_URL, echo=False)
    
    async def init_db(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)
    
    async def get_session(self):
        async with AsyncSession(self.engine) as session:
            yield session

database = DataBase()