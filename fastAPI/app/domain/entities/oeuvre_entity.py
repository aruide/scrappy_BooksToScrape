from dataclasses import dataclass
from typing import Optional

@dataclass
class OeuvreEntity:
    """
    Entité représentant une œuvre.

    Attributes:
        id_oeuvre (Optional[int]): Identifiant unique de l'œuvre.
        title (str): Titre de l'œuvre.
        description (Optional[str]): Description de l'œuvre.
        rating (int): Note ou évaluation de l'œuvre.
        upc (str): Code UPC unique.
        prix_ht (float): Prix hors taxe.
        taxe (float): Taux de taxe appliqué au prix.
        nb_available (int): Nombre d'exemplaires disponibles.
        nb_review (int): Nombre de critiques ou avis.
        image_url (str): URL de l'image représentant l'œuvre.
        genre_fk (int): Clé étrangère vers le genre de l'œuvre.
    """
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
