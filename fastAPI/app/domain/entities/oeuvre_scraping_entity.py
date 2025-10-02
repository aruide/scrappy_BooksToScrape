from dataclasses import dataclass
from typing import Optional

@dataclass
class OeuvreScrapingEntity:
    oeuvre_fk: int
    scraping_log_fk: int