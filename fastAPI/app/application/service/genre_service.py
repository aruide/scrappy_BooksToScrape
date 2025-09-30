from typing import List
from app.domain.repositories.genre_repository import GenreRepository

class GenreService:
    def __init__(self, repository: GenreRepository):
        self.repository = repository

    async def list_all_genre(self) -> List:
        return await self.repository.get_all()