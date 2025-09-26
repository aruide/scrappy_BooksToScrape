# booksToScrape/pipeline/genre_pipeline.py
import logging
from sqlmodel import SQLModel, Field, create_engine, Session
from booksToScrape.item.genre_item import GenreItem 
from booksToScrape.settings import DATABASE_URL
from booksToScrape.model.genre import Genre

logger = logging.getLogger(__name__)

class GenrePipeline:
    def __init__(self):
        self.engine = create_engine(DATABASE_URL, echo=True)  # echo=True pour debug
        # création des tables si elles n'existent pas
        SQLModel.metadata.create_all(self.engine)
        logger.info("Pipeline Genre initialisée et tables créées")

    def open_spider(self, spider):
        logger.info("Ouverture du pipeline…")

    def close_spider(self, spider):
        logger.info("Fermeture du pipeline…")

    def process_item(self, item, spider):
        
        with Session(self.engine) as session:
            # On vérifie si le genre existe déjà pour éviter les doublons
            existing = session.query(Genre).filter(Genre.name == item["name"]).first()
            if existing:
                logger.info(f"Genre déjà existant : {existing.name} (id={existing.id_genre})")
                return item

            # Insertion du genre
            genre = Genre.from_item(item)
            session.add(genre)
            session.commit()
            session.refresh(genre)  # récupère l'id auto-généré
            logger.info(f"Genre inséré : {genre.name}")
        return item
