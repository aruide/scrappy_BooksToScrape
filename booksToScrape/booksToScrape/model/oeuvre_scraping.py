from sqlmodel import SQLModel, Field
from datetime import datetime

class OeuvreScraping(SQLModel, table=True):
    __tablename__ = "oeuvre_scrapping"
    oeuvre_fk: int = Field(foreign_key="oeuvre.id_oeuvre", primary_key=True)
    scraping_log_fk: int = Field(foreign_key="scraping_logs.id_scraping_log", primary_key=True)
