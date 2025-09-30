# booksToScrape/pipeline/oeuvre_pipeline.py
import logging
from sqlmodel import SQLModel, Field, Session, select, create_engine
from booksToScrape.item.oeuvre_item import OeuvreItem
from booksToScrape.model.genre import Genre
from booksToScrape.model.oeuvre import Oeuvre
from booksToScrape.model.scraping_logs import ScrapingLogs
from booksToScrape.model.exchange_rates import ExchangeRates
from booksToScrape.settings import DATABASE_URL
from datetime import datetime
import requests

logger = logging.getLogger(__name__)

class OeuvrePipeline:
    def __init__(self):
        # echo=False => désactive le spam SQLAlchemy
        self.engine = create_engine(DATABASE_URL, echo=False)
        SQLModel.metadata.create_all(self.engine)
        self.scraping_log_id = None

    def open_spider(self, spider):
        logger.info("Pipeline Oeuvre ouvert.")
        try:
            response = requests.get("https://latest.currency-api.pages.dev/v1/currencies/gbp.json")
            response.raise_for_status()
            data = response.json()
            current_rate_value = data["gbp"]["eur"]  # taux EUR
            logger.info(f"Taux de change GBP -> EUR récupéré : {current_rate_value}")
        except Exception as e:
            logger.warning(f"Impossible de récupérer le taux de change, valeur par défaut utilisée : {e}")
            current_rate_value = 1.15  # fallback si l'API échoue
        with Session(self.engine) as session:
            stmt = select(ExchangeRates).where(
                ExchangeRates.base_currency == "GBP",
                ExchangeRates.target_currency == "EUR"
            )
            rate_obj = session.exec(stmt).first()
            if not rate_obj:
                rate_obj = ExchangeRates(
                    base_currency="GBP",
                    target_currency="EUR",
                    rate=current_rate_value,
                    retrieved_at=datetime.utcnow()
                )
                session.add(rate_obj)
                session.commit()
                session.refresh(rate_obj)

            scraping_log = ScrapingLogs(
                scraped_at=datetime.utcnow(),
                site_url="http://books.toscrape.com",
                exchange_rate_fk=rate_obj.id_exchange_rate
            )
            session.add(scraping_log)
            session.commit()
            session.refresh(scraping_log)
            self.scraping_log_id = scraping_log.id_scraping_log

    def close_spider(self, spider):
        logger.info("Pipeline Oeuvre fermé.")

    def process_item(self, item, spider):
        try:
            with Session(self.engine) as session:
                # Cherche le genre par son nom
                stmt = select(Genre).where(Genre.name == item['genre'])
                genre_obj = session.exec(stmt).first()
                if not genre_obj:
                    genre_obj = Genre(name=item['genre'])
                    session.add(genre_obj)
                    session.commit()
                    session.refresh(genre_obj)

                # Crée l’œuvre avec la FK genre et le scraping_log
                oeuvre = Oeuvre.from_item(item, genre_obj.id_genre)
                oeuvre.scraping_logs_fk = self.scraping_log_id  # association au scraping_log
                session.add(oeuvre)
                session.commit()
                logger.info(f"Oeuvre insérée : {oeuvre.title}")

        except Exception as e:
            logger.info(f"Erreur insertion oeuvre: {e}")

        return item
