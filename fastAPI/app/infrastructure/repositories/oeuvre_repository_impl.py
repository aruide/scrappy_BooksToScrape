from sqlmodel import select
from typing import List
from sqlalchemy import func
from sqlmodel.ext.asyncio.session import AsyncSession

from app.domain.repositories.oeuvre_repository import OeuvreRepository
from app.domain.entities.oeuvre_entity import OeuvreEntity
from app.domain.dto.oeuvre_response import OeuvreDTO, PriceOeuvreByGenreDTO, NumberOeuvreByGenreDTO
from app.infrastructure.db.oeuvre import Oeuvre
from app.infrastructure.db.genre import Genre
from app.infrastructure.db.scraping_logs import ScrapingLogs
from app.infrastructure.db.exchange_rates import ExchangeRates
from app.infrastructure.db.oeuvre_scraping import OeuvreScraping

class OeuvreRepositoryImpl(OeuvreRepository):
    """
    Implémentation concrète du repository pour les oeuvres.

    Attributes:
        session (AsyncSession): Session asynchrone SQLAlchemy/SQLModel pour la DB.
    """

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self) -> List[OeuvreDTO]:
        """
        Récupère toutes les oeuvres avec leur genre, taux de change et date de scraping.

        Returns:
            List[OeuvreDTO]: Liste des oeuvres DTO.
        """
        statement = (
            select(Oeuvre, Genre.name, ExchangeRates.rate, ScrapingLogs.scraped_at)
            .join(Genre, Genre.id_genre == Oeuvre.genre_fk)
            .join(OeuvreScraping, OeuvreScraping.oeuvre_fk == Oeuvre.id_oeuvre)
            .join(ScrapingLogs, ScrapingLogs.id_scraping_log == OeuvreScraping.scraping_log_fk)
            .join(ExchangeRates, ExchangeRates.id_exchange_rate == ScrapingLogs.exchange_rate_fk)
        )
        result = await self.session.exec(statement)
        return [OeuvreDTO.from_model(o, genre_name, rate, scraped_at) for o, genre_name, rate, scraped_at in result.all()]

    async def get_oeuvres_by_upc(self, upc: str) -> List[OeuvreDTO]:
        """
        Récupère les oeuvres correspondant à un UPC partiel ou complet.

        Args:
            upc (str): UPC recherché.

        Returns:
            List[OeuvreDTO]: Liste des oeuvres correspondantes.
        """
        statement = (
            select(Oeuvre, Genre.name, ExchangeRates.rate, ScrapingLogs.scraped_at)
            .join(Genre, Genre.id_genre == Oeuvre.genre_fk)
            .join(OeuvreScraping, OeuvreScraping.oeuvre_fk == Oeuvre.id_oeuvre)
            .join(ScrapingLogs, ScrapingLogs.id_scraping_log == OeuvreScraping.scraping_log_fk)
            .join(ExchangeRates, ExchangeRates.id_exchange_rate == ScrapingLogs.exchange_rate_fk)
            .where(Oeuvre.upc.like(f"%{upc}%"))
        )
        result = await self.session.exec(statement)
        return [OeuvreDTO.from_model(o, genre_name, rate, scraped_at) for o, genre_name, rate, scraped_at in result.all()]

    async def get_by_genre(self, genre_name: str) -> List[OeuvreDTO]:
        """
        Récupère toutes les oeuvres d'un genre spécifique.

        Args:
            genre_name (str): Nom du genre.

        Returns:
            List[OeuvreDTO]: Liste des oeuvres filtrées par genre.
        """
        statement = (
            select(Oeuvre, Genre.name, ExchangeRates.rate, ScrapingLogs.scraped_at)
            .join(Genre, Genre.id_genre == Oeuvre.genre_fk)
            .join(OeuvreScraping, OeuvreScraping.oeuvre_fk == Oeuvre.id_oeuvre)
            .join(ScrapingLogs, ScrapingLogs.id_scraping_log == OeuvreScraping.scraping_log_fk)
            .join(ExchangeRates, ExchangeRates.id_exchange_rate == ScrapingLogs.exchange_rate_fk)
            .where(Genre.name == genre_name)
        )
        result = await self.session.exec(statement)
        return [OeuvreDTO.from_model(o, genre_name, rate, scraped_at) for o, genre_name, rate, scraped_at in result.all()]

    async def get_between_prices(self, min_value: float, max_value: float) -> List[OeuvreDTO]:
        """
        Récupère les oeuvres dont le prix TTC est compris entre min_value et max_value.

        Args:
            min_value (float): Prix minimum.
            max_value (float): Prix maximum.

        Returns:
            List[OeuvreDTO]: Liste des oeuvres filtrées par prix.
        """
        statement = (
            select(Oeuvre, Genre.name, ExchangeRates.rate, ScrapingLogs.scraped_at)
            .join(Genre, Genre.id_genre == Oeuvre.genre_fk)
            .join(OeuvreScraping, OeuvreScraping.oeuvre_fk == Oeuvre.id_oeuvre)
            .join(ScrapingLogs, ScrapingLogs.id_scraping_log == OeuvreScraping.scraping_log_fk)
            .join(ExchangeRates, ExchangeRates.id_exchange_rate == ScrapingLogs.exchange_rate_fk)
            .where((Oeuvre.prix_ht * (1 + Oeuvre.taxe)).between(min_value, max_value))
        )
        result = await self.session.exec(statement)
        return [OeuvreDTO.from_model(o, genre_name, rate, scraped_at) for o, genre_name, rate, scraped_at in result.all()]

    async def get_avg_price_by_genre(self) -> List[PriceOeuvreByGenreDTO]:
        """
        Calcule le prix TTC moyen par genre et le taux de change minimum associé.

        Returns:
            List[PriceOeuvreByGenreDTO]: Liste des prix moyens par genre.
        """
        prix_ttc = func.avg(Oeuvre.prix_ht * (1 + Oeuvre.taxe)).label("prix_ttc")
        single_rate = func.min(ExchangeRates.rate).label("exchange_rate")
        statement = (
            select(Genre.name, prix_ttc, single_rate)
            .join(Genre, Genre.id_genre == Oeuvre.genre_fk)
            .join(OeuvreScraping, OeuvreScraping.oeuvre_fk == Oeuvre.id_oeuvre)
            .join(ScrapingLogs, ScrapingLogs.id_scraping_log == OeuvreScraping.scraping_log_fk)
            .join(ExchangeRates, ExchangeRates.id_exchange_rate == ScrapingLogs.exchange_rate_fk)
            .group_by(Genre.name)
            .order_by(prix_ttc.desc())
        )
        result = await self.session.exec(statement)
        return [PriceOeuvreByGenreDTO.from_model(o, genre_name, rate) for o, genre_name, rate in result.all()]

    async def get_number_by_genre(self) -> List[NumberOeuvreByGenreDTO]:
        """
        Compte le nombre d'oeuvres par genre.

        Returns:
            List[NumberOeuvreByGenreDTO]: Liste du nombre d'oeuvres par genre.
        """
        nb_oeuvre = func.count(Oeuvre.id_oeuvre).label("nb_oeuvre")
        statement = (
            select(Genre.name, nb_oeuvre)
            .join(Genre, Genre.id_genre == Oeuvre.genre_fk)
            .group_by(Genre.name)
            .order_by(nb_oeuvre.desc())
        )
        result = await self.session.exec(statement)
        return [NumberOeuvreByGenreDTO.from_model(o, nb_oeuvre) for o, nb_oeuvre in result.all()]
