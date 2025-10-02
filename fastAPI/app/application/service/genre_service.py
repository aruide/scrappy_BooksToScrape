from typing import List
from app.domain.repositories.genre_repository import GenreRepository

class GenreService:
    """
    Service pour gérer les opérations liées aux genres.
    """

    def __init__(self, repository: GenreRepository):
        """
        Initialise le service avec un repository de genres.

        Args:
            repository (GenreRepository): Le repository pour accéder aux genres.
        """
        self.repository = repository

    async def list_all_genre(self) -> List:
        """
        Récupère la liste de tous les genres.

        Returns:
            List: Liste des genres.
        """
        return await self.repository.get_all()
