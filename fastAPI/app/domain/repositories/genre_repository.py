from typing import List
from app.domain.entities.genre_entity import GenreEntity
from abc import ABC, abstractmethod

class GenreRepository(ABC):
    @abstractmethod
    async def get_all(self) -> List:
        raise NotImplementedError
