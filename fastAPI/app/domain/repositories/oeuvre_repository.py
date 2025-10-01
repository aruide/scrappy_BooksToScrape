from typing import List
from app.domain.dto.oeuvre_response import OeuvreDTO, PriceOeuvreByGenreDTO, NumberOeuvreByGenreDTO

class OeuvreRepository:
    async def get_all(self) -> List[OeuvreDTO]:
        raise NotImplementedError
    
    async def get_oeuvres_by_upc(self, upc) -> List[OeuvreDTO]:
        raise NotImplementedError

    async def get_by_genre(self, genre: str) -> List[OeuvreDTO]:
        raise NotImplementedError

    async def get_between_prices(self, min_value: float, max_value: float) -> List[OeuvreDTO]:
        raise NotImplementedError

    async def get_avg_price_by_genre(self) -> List[PriceOeuvreByGenreDTO]:
        raise NotImplementedError

    async def get_number_by_genre(self) -> List[NumberOeuvreByGenreDTO]:
        raise NotImplementedError
    