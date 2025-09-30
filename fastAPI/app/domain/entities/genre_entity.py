from dataclasses import dataclass
from typing import Optional

@dataclass
class GenreEntity:
    id_genre: Optional[int]
    name: str