from datetime import datetime      
from dataclasses import dataclass
from typing import Optional

@dataclass
class ExchangeRatesEntity:
    id_exchange_rate: Optional[int]
    base_currency: str
    target_currency: str
    rate: float
    retrieved_at: datetime