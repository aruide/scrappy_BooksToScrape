from sqlmodel import SQLModel, Field
from datetime import datetime

class ExchangeRates(SQLModel, table=True):
    __tablename__ = "exchange_rates"
    id_exchange_rate: int | None = Field(default=None, primary_key=True)
    base_currency: str
    target_currency: str
    rate: float
    retrieved_at: datetime = Field(default_factory=datetime.utcnow)
