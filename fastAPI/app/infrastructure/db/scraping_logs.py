from sqlmodel import SQLModel, Field
from datetime import datetime

class ScrapingLogs(SQLModel, table=True):
    """
    Modèle représentant un log de scraping.

    Attributes:
        id_scraping_log (int | None): Identifiant unique du log.
        scraped_at (datetime): Date et heure du scraping.
        site_url (str): URL du site scrappé.
        exchange_rate_fk (int): Clé étrangère vers la table ExchangeRates.
    """

    __tablename__ = "scraping_logs"

    id_scraping_log: int | None = Field(default=None, primary_key=True)
    scraped_at: datetime = Field(default_factory=datetime.utcnow)
    site_url: str
    exchange_rate_fk: int = Field(foreign_key="exchange_rates.id_exchange_rate")
