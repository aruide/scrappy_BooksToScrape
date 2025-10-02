# booksToScrape/pipeline/oeuvre_pipeline.py
import logging
from sqlmodel import SQLModel, Field, Session, select, create_engine
from booksToScrape.item.oeuvre_item import OeuvreItem
from booksToScrape.model.genre import Genre
from booksToScrape.model.oeuvre import Oeuvre
from booksToScrape.model.scraping_logs import ScrapingLogs
from booksToScrape.model.exchange_rates import ExchangeRates
from booksToScrape.model.oeuvre_scraping import OeuvreScraping
from booksToScrape.settings import DATABASE_URL
from datetime import datetime
import requests

logger = logging.getLogger(__name__)

class OeuvrePipeline:
    def __init__(self):
        self.engine = create_engine(DATABASE_URL, echo=False)
        SQLModel.metadata.create_all(self.engine)
        self.scraping_log_id = None

    def open_spider(self, spider):
        logger.info("Pipeline Oeuvre ouvert.")
        try:
            response = requests.get("https://latest.currency-api.pages.dev/v1/currencies/gbp.json")
            response.raise_for_status()
            data = response.json()
            current_rate_value = data["gbp"]["eur"]
            logger.info(f"Taux de change GBP -> EUR récupéré : {current_rate_value}")
        except Exception as e:
            logger.warning(f"Impossible de récupérer le taux de change, valeur par défaut utilisée : {e}")
            current_rate_value = 1.15  # fallback

        with Session(self.engine) as session:
            # Récupère ou crée le taux de change
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

            # Crée le scraping log
            scraping_log = ScrapingLogs(
                scraped_at=datetime.utcnow(),
                site_url="http://books.toscrape.com",
                exchange_rate_fk=rate_obj.id_exchange_rate
            )
            session.add(scraping_log)
            session.commit()
            session.refresh(scraping_log)
            self.scraping_log_id = scraping_log.id_scraping_log

            if self.scraping_log_id is None:
                raise RuntimeError("Impossible de créer le scraping_log. Pipeline arrêté.")

    def close_spider(self, spider):
        logger.info("Pipeline Oeuvre fermé.")

    def process_item(self, item, spider):
        try:
            with Session(self.engine) as session:
                # 1️⃣ Cherche ou crée le genre
                stmt = select(Genre).where(Genre.name == item['genre'])
                genre_obj = session.exec(stmt).first()
                if not genre_obj:
                    genre_obj = Genre(name=item['genre'])
                    session.add(genre_obj)
                    session.commit()
                    session.refresh(genre_obj)

                # 2️⃣ Cherche l’œuvre existante par UPC
                stmt = select(Oeuvre).where(Oeuvre.upc == item['upc'])
                existing_oeuvre = session.exec(stmt).first()

                # 3️⃣ Crée une nouvelle oeuvre si nécessaire
                new_oeuvre = Oeuvre.from_item(item, genre_obj.id_genre)

                create_new = False
                if existing_oeuvre:
                    # Méthode .equals() pour comparer automatiquement tous les champs
                    if not self.oeuvre_equals(existing_oeuvre, new_oeuvre):
                        create_new = True
                else:
                    create_new = True

                if create_new:
                    session.add(new_oeuvre)
                    session.commit()
                    session.refresh(new_oeuvre)
                    oeuvre_to_link = new_oeuvre
                    logger.info(f"Oeuvre insérée : {new_oeuvre.title}")
                else:
                    oeuvre_to_link = existing_oeuvre
                    logger.info(f"Oeuvre existante, pas de modification : {existing_oeuvre.title}")

                # 4️⃣ Crée l’association OeuvreScraping
                oeuvre_scraping = OeuvreScraping(
                    oeuvre_fk=oeuvre_to_link.id_oeuvre,
                    scraping_log_fk=self.scraping_log_id
                )
                session.add(oeuvre_scraping)
                session.commit()

        except Exception as e:
            logger.exception(f"Erreur insertion oeuvre: {e}")

        return item

    @staticmethod
    def oeuvre_equals(a: Oeuvre, b: Oeuvre) -> bool:
        """
        Compare toutes les colonnes sauf id, genre_fk et scraping_logs_fk.
        Retourne True si toutes les valeurs sont identiques.
        """
        exclude = {"id_oeuvre", "genre_fk", "scraping_logs_fk"}
        for k, v in a.dict().items():
            if k in exclude:
                continue
            if getattr(b, k) != v:
                return False
        return True
