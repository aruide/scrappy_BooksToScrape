from dataclasses import dataclass
from app.domain.entities.oeuvre_entity import OeuvreEntity
from datetime import datetime

@dataclass
class OeuvreDTO:
    """
    Data Transfer Object pour représenter une œuvre avec informations
    supplémentaires telles que le genre, le taux de change et la date de scraping.
    """
    id_oeuvre: int
    title: str
    description: str
    rating: int
    upc: str
    prix_ht: float
    taxe: float
    nb_available: int
    nb_review: int
    image_url: str
    genre: str
    exchange_eur: float
    scraped_at: datetime

    @property
    def prix_ttc(self) -> float:
        """
        Calcule le prix TTC de l'œuvre.

        Returns:
            float: Prix TTC.
        """
        return self.prix_ht * (1 + self.taxe)

    @property
    def prix_ttc_euro(self) -> float:
        """
        Calcule le prix TTC converti en euros.

        Returns:
            float: Prix TTC en euros.
        """
        return self.prix_ttc * self.exchange_eur
    
    @classmethod
    def from_model(cls, o: OeuvreEntity, genre_name: str, rate: float, scraped_at: datetime):
        """
        Crée un OeuvreDTO à partir d'une entité OeuvreEntity et informations associées.

        Args:
            o (OeuvreEntity): L'entité œuvre.
            genre_name (str): Nom du genre.
            rate (float): Taux de change vers l'euro.
            scraped_at (datetime): Date du scraping.

        Returns:
            OeuvreDTO: Objet DTO complet.
        """
        return cls(
            id_oeuvre=o.id_oeuvre,
            title=o.title,
            description=o.description,
            rating=o.rating,
            upc=o.upc,
            prix_ht=o.prix_ht,
            taxe=o.taxe,
            nb_available=o.nb_available,
            nb_review=o.nb_review,
            image_url=o.image_url,
            genre=genre_name,
            exchange_eur=rate,
            scraped_at=scraped_at
        )


@dataclass
class PriceOeuvreByGenreDTO:
    """
    DTO représentant le prix moyen TTC d'œuvres par genre.
    """
    genre: str
    prix_ttc_avg: float
    exchange_eur: float

    @property
    def prix_ttc_avg_euro(self) -> float:
        """
        Calcule le prix moyen TTC converti en euros.

        Returns:
            float: Prix moyen TTC en euros.
        """
        return self.prix_ttc_avg * self.exchange_eur
    
    @classmethod
    def from_model(cls, genre: str, prix_ttc_avg: float, exchange_eur: float):
        """
        Crée un PriceOeuvreByGenreDTO à partir des valeurs calculées.

        Args:
            genre (str): Nom du genre.
            prix_ttc_avg (float): Prix TTC moyen.
            exchange_eur (float): Taux de change vers l'euro.

        Returns:
            PriceOeuvreByGenreDTO: Objet DTO complet.
        """
        return cls(
            genre=genre,
            prix_ttc_avg=prix_ttc_avg,
            exchange_eur=exchange_eur
        )


@dataclass
class NumberOeuvreByGenreDTO:
    """
    DTO représentant le nombre d'œuvres par genre.
    """
    genre: str
    number_oeuvre: int

    @classmethod
    def from_model(cls, genre: str, number_oeuvre: int):
        """
        Crée un NumberOeuvreByGenreDTO à partir des valeurs calculées.

        Args:
            genre (str): Nom du genre.
            number_oeuvre (int): Nombre d'œuvres dans le genre.

        Returns:
            NumberOeuvreByGenreDTO: Objet DTO complet.
        """
        return cls(
            genre=genre,
            number_oeuvre=number_oeuvre
        )
