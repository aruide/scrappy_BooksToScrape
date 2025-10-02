from datetime import datetime
from dataclasses import dataclass
from typing import Optional

@dataclass
class ScrapingLogsEntity:
    id_scraping_log: Optional[int]
    scraped_at: datetime
    site_url: str
    exchange_rate_fk: Optional[int]
