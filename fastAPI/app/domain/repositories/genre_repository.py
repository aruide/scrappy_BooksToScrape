from typing import List
from app.domain.entities.genre_entity import GenreEntity
from abc import ABC, abstractmethod

class GenreRepository(ABC):
    """
    Interface abstraite pour le repository des genres.
    Définit les opérations disponibles pour manipuler les genres.
    """

    @abstractmethod
    async def get_all(self) -> List[GenreEntity]:
        """
        Récupère tous les genres existants.

        Returns:
            List[GenreEntity]: Liste de tous les genres.
        """
        raise NotImplementedError
