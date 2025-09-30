from typing import List
from app.domain.entities.oeuvre_entity import OeuvreEntity
from app.domain.repositories.oeuvre_repository import OeuvreRepository

class OeuvreService:
    def __init__(self, repository: OeuvreRepository):
        self.repository = repository

    async def list_all_oeuvres(self) -> List[OeuvreEntity]:
        return await self.repository.get_all()

    async def list_by_genre(self, genre: str) -> List[OeuvreEntity]:
        return await self.repository.get_by_genre(genre)

    async def list_by_price_between(self, min_value: float, max_value: float) -> List[OeuvreEntity]:
        return await self.repository.get_between_prices(min_value, max_value)

    async def avg_price_by_genre(self):
        return await self.repository.get_avg_price_by_genre()

    async def count_by_genre(self):
        return await self.repository.get_number_by_genre()
