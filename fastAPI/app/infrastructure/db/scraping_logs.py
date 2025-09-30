from sqlmodel import SQLModel, Field
from datetime import datetime

class ScrapingLogs(SQLModel, table=True):
    __tablename__ = "scraping_logs"
    id_scraping_log: int | None = Field(default=None, primary_key=True)
    scraped_at: datetime = Field(default_factory=datetime.utcnow)
    site_url: str
    exchange_rate_fk: int = Field(foreign_key="exchange_rates.id_exchange_rate")