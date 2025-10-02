# booksToScrape/pipeline/oeuvre_pipeline.py
from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession
import os
from dotenv import load_dotenv
from pathlib import Path

# Chargement des variables d'environnement depuis le fichier .env
env_path = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

print(f"Environnement : {env_path}")

DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWD = os.getenv("DATABASE_PASSWD")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_IP = os.getenv("DATABASE_IP")

DATABASE_URL = (
    f"postgresql+asyncpg://{DATABASE_USER}:{DATABASE_PASSWD}"
    f"@{DATABASE_IP}:{DATABASE_PORT}/{DATABASE_NAME}"
)

class DataBase:
    """
    Gestion de la connexion à la base de données principale.
    """

    def __init__(self):
        """
        Initialise l'engine SQLAlchemy pour la base de données asynchrone.
        """
        self.engine = create_async_engine(DATABASE_URL, echo=False)
    
    async def init_db(self):
        """
        Crée toutes les tables définies dans SQLModel.
        """
        async with self.engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)

# Instance globale pour l'accès à la DB
database = DataBase()

async def get_session():
    """
    Fournit une session asynchrone pour interagir avec la base de données principale.

    Yields:
        AsyncSession: Session SQLModel asynchrone.
    """
    async with AsyncSession(database.engine) as session:
        yield session

# --- Partie pour les tests ---

TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"
test_engine = create_async_engine(TEST_DATABASE_URL, echo=False)

async def init_test_db():
    """
    Initialise la base SQLite en mémoire pour les tests.
    Crée toutes les tables définies dans SQLModel.
    """
    async with test_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

async def get_test_session():
    """
    Fournit une session asynchrone pour les tests.

    Yields:
        AsyncSession: Session SQLModel asynchrone pour la base de test.
    """
    async with AsyncSession(test_engine) as session:
        yield session
