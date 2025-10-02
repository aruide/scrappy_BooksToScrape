from datetime import datetime
from dataclasses import dataclass
from typing import Optional

@dataclass
class ExchangeRatesEntity:
    """
    Entité représentant un taux de change entre deux devises.

    Attributes:
        id_exchange_rate (Optional[int]): Identifiant unique du taux de change.
        base_currency (str): Devise de base.
        target_currency (str): Devise cible.
        rate (float): Valeur du taux de change (base → cible).
        retrieved_at (datetime): Date et heure de récupération du taux.
    """
    id_exchange_rate: Optional[int]
    base_currency: str
    target_currency: str
    rate: float
    retrieved_at: datetime
