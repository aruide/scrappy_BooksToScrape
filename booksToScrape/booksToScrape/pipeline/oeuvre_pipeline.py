# booksToScrape/pipeline/oeuvre_pipeline.py
import logging
from sqlmodel import SQLModel, Field, Session, select, create_engine
from booksToScrape.item.oeuvre_item import OeuvreItem
from booksToScrape.model.genre import Genre
from booksToScrape.model.oeuvre import Oeuvre
from booksToScrape.settings import DATABASE_URL

logger = logging.getLogger(__name__)

class OeuvrePipeline:
    def __init__(self):
        # echo=False => désactive le spam SQLAlchemy
        self.engine = create_engine(DATABASE_URL, echo=False)
        SQLModel.metadata.create_all(self.engine)

    def open_spider(self, spider):
        logger.info("Pipeline Oeuvre ouvert.")

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

                # Crée l’œuvre avec la FK genre
                oeuvre = Oeuvre.from_item(item, genre_obj.id_genre)
                session.add(oeuvre)
                session.commit()
                logger.info(f"Oeuvre insérée : {oeuvre.title}")

        except Exception as e:
            logger.info(f"Erreur insertion oeuvre: {e}")

        return item
