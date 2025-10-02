from sqlmodel import select
from typing import List
from sqlmodel.ext.asyncio.session import AsyncSession

from app.domain.repositories.genre_repository import GenreRepository
from app.infrastructure.db.genre import Genre

class GenreRepositoryImpl(GenreRepository):
    """
    Implémentation du repository pour la gestion des genres.
    
    Attributes:
        session (AsyncSession): Session asynchrone pour interagir avec la base de données.
    """

    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def get_all(self) -> List[str]:
        """
        Récupère tous les noms de genres existants.

        Returns:
            List[str]: Liste des noms de genres.
        """
        statement = select(Genre.name)
        result = await self.session.exec(statement)
        return [name for name in result.all()]
