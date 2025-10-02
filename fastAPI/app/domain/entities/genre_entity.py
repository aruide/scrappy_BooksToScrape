from dataclasses import dataclass
from typing import Optional

@dataclass
class GenreEntity:
    """
    Entité représentant un genre d'œuvre.

    Attributes:
        id_genre (Optional[int]): Identifiant unique du genre.
        name (str): Nom du genre.
    """
    id_genre: Optional[int]
    name: str
