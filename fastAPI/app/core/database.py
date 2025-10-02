# booksToScrape/pipeline/oeuvre_pipeline.py
from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession
import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

print(f"environnement : {env_path}")

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
    
database = DataBase()

async def get_session():
    async with AsyncSession(database.engine) as session:
        yield session
        
# --- Partie pour les tests ---
# Engine SQLite en mémoire pour tests
TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"
test_engine = create_async_engine(TEST_DATABASE_URL, echo=False)

async def init_test_db():
    async with test_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

async def get_test_session():
    async with AsyncSession(test_engine) as session:
        yield session