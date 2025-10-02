from sqlmodel import SQLModel, Field

class OeuvreScraping(SQLModel, table=True):
    """
    Modèle représentant la relation entre une oeuvre et un log de scraping.
    
    Attributes:
        oeuvre_fk (int): Identifiant de l'oeuvre (clé étrangère vers Oeuvre).
        scraping_log_fk (int): Identifiant du log de scraping (clé étrangère vers ScrapingLogs).
    """

    __tablename__ = "oeuvre_scrapping"

    oeuvre_fk: int = Field(foreign_key="oeuvre.id_oeuvre", primary_key=True)
    scraping_log_fk: int = Field(foreign_key="scraping_logs.id_scraping_log", primary_key=True)
