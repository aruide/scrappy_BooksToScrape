from sqlmodel import select
from typing import List
from sqlalchemy import func
from sqlmodel.ext.asyncio.session import AsyncSession

from app.domain.repositories.oeuvre_repository import OeuvreRepository
from app.domain.entities.oeuvre_entity import OeuvreEntity
from app.domain.entities.genre_entity import GenreEntity
from app.domain.dto.oeuvre_response import *
from app.infrastructure.db.oeuvre import Oeuvre
from app.infrastructure.db.genre import Genre
from app.infrastructure.db.scraping_logs import ScrapingLogs
from app.infrastructure.db.exchange_rates import ExchangeRates
from app.infrastructure.db.oeuvre_scraping import OeuvreScraping

class OeuvreRepositoryImpl(OeuvreRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def get_all(self) -> List[OeuvreDTO]:
        statement = ( select(Oeuvre, Genre.name, ExchangeRates.rate)
                    .join(Genre, Genre.id_genre == Oeuvre.genre_fk)
                    .join(OeuvreScraping, OeuvreScraping.oeuvre_fk == Oeuvre.id_oeuvre)
                    .join(ScrapingLogs, ScrapingLogs.id_scraping_log == OeuvreScraping.scraping_log_fk)
                    .join(ExchangeRates, ExchangeRates.id_exchange_rate == ScrapingLogs.exchange_rate_fk)
                 )
        result = await self.session.exec(statement)
        return [OeuvreDTO.from_model(o, genre_name, rate) for o, genre_name, rate in result.all()]
    
    async def get_by_genre(self, genre_name: str) -> List[OeuvreDTO] :
        statement = ( select(Oeuvre, Genre.name, ExchangeRates.rate)
                    .join(Genre, Genre.id_genre == Oeuvre.genre_fk)
                    .join(OeuvreScraping, OeuvreScraping.oeuvre_fk == Oeuvre.id_oeuvre)
                    .join(ScrapingLogs, ScrapingLogs.id_scraping_log == OeuvreScraping.scraping_log_fk)
                    .join(ExchangeRates, ExchangeRates.id_exchange_rate == ScrapingLogs.exchange_rate_fk)
                    .where(Genre.name == genre_name)
                )
        result = await self.session.exec(statement)
        return [OeuvreDTO.from_model(o, genre_name, rate) for o, genre_name, rate in result.all()]
    
    async def get_between_prices(self, min_value: float, max_value: float) -> List[OeuvreDTO]:
        statement = ( select(Oeuvre, Genre.name, ExchangeRates.rate)
                    .join(Genre, Genre.id_genre == Oeuvre.genre_fk)
                    .join(OeuvreScraping, OeuvreScraping.oeuvre_fk == Oeuvre.id_oeuvre)
                    .join(ScrapingLogs, ScrapingLogs.id_scraping_log == OeuvreScraping.scraping_log_fk)
                    .join(ExchangeRates, ExchangeRates.id_exchange_rate == ScrapingLogs.exchange_rate_fk)
                    .where((Oeuvre.prix_ht * (1 + Oeuvre.taxe))
                        .between(min_value, max_value)) 
                )
        result = await self.session.exec(statement)
        return [OeuvreDTO.from_model(o, genre_name, rate) for o, genre_name, rate in result.all()]
    
    async def get_avg_price_by_genre(self):
        prix_ttc = func.avg(Oeuvre.prix_ht * (1 + Oeuvre.taxe)).label("prix_ttc")
        single_rate = func.min(ExchangeRates.rate).label("exchange_rate")
    
        statement = ( select(Genre.name, prix_ttc, single_rate)
                    .join(Genre, Genre.id_genre == Oeuvre.genre_fk)
                    .join(OeuvreScraping, OeuvreScraping.oeuvre_fk == Oeuvre.id_oeuvre)
                    .join(ScrapingLogs, ScrapingLogs.id_scraping_log == OeuvreScraping.scraping_log_fk)
                    .join(ExchangeRates, ExchangeRates.id_exchange_rate == ScrapingLogs.exchange_rate_fk)
                    .group_by(Genre.name)
                    .order_by(prix_ttc.desc())
                    )
        result = await self.session.exec(statement)
        return [PriceOeuvreByGenreDTO.from_model(o, genre_name, rate) for o, genre_name, rate in result.all()]
    
    async def get_number_by_genre(self):
        nb_oeuvre = func.count(Oeuvre.id_oeuvre).label("nb_oeuvre")
    
        statement = ( select(Genre.name, nb_oeuvre)
                    .join(Genre, Genre.id_genre == Oeuvre.genre_fk)
                    .group_by(Genre.name)
                    .order_by(nb_oeuvre.desc())
                    )
        result = await self.session.exec(statement)
        return [NumberOeuvreByGenreDTO.from_model(o, nb_oeuvre) for o, nb_oeuvre in result.all()]
    