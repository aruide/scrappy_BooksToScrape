from dataclasses import dataclass
from typing import Optional

@dataclass
class OeuvreEntity:
    id_oeuvre: Optional[int]
    title: str
    description: Optional[str]
    rating: int
    upc: str
    prix_ht: float
    taxe: float
    nb_available: int
    nb_review: int
    image_url: str
    genre_fk: int