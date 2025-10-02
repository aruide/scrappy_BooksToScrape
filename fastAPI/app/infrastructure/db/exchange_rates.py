from sqlmodel import SQLModel, Field
from datetime import datetime

class ExchangeRates(SQLModel, table=True):
    """
    Modèle représentant un taux de change.

    Attributes:
        id_exchange_rate (int | None): Identifiant unique du taux de change.
        base_currency (str): Devise de base.
        target_currency (str): Devise cible.
        rate (float): Taux de change.
        retrieved_at (datetime): Date et heure de récupération du taux.
    """
    __tablename__ = "exchange_rates"

    id_exchange_rate: int | None = Field(default=None, primary_key=True)
    base_currency: str
    target_currency: str
    rate: float
    retrieved_at: datetime = Field(default_factory=datetime.utcnow)
