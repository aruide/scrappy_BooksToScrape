from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class ScrapingLogsEntity:
    """
    Entité représentant un log de scraping.

    Attributes:
        id_scraping_log (Optional[int]): Identifiant unique du log de scraping.
        scraped_at (datetime): Date et heure du scraping.
        site_url (str): URL du site scrappé.
        exchange_rate_fk (Optional[int]): Clé étrangère vers le taux de change utilisé lors du scraping.
    """
    id_scraping_log: Optional[int]
    scraped_at: datetime
    site_url: str
    exchange_rate_fk: Optional[int]
