from dataclasses import dataclass
from app.domain.entities.oeuvre_entity import OeuvreEntity

@dataclass
class OeuvreDTO:
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

    @property
    def prix_ttc(self) -> float:
        return self.prix_ht * (1 + self.taxe)

    @property
    def prix_ttc_euro(self) -> float:
        return self.prix_ttc * self.exchange_eur
    
    @classmethod
    def from_model(cls, o: OeuvreEntity, genre_name, rate):
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
            exchange_eur=rate
        )


@dataclass
class PriceOeuvreByGenreDTO:
    genre: str
    prix_ttc_avg: float
    exchange_eur: float

    @property
    def prix_ttc_avg_euro(self) -> float:
        return self.prix_ttc_avg * self.exchange_eur
    
    @classmethod
    def from_model(cls, genre, prix_ttc_avg, exchange_eur):
        return cls(
            genre = genre,
            prix_ttc_avg = prix_ttc_avg,
            exchange_eur = exchange_eur
        )

@dataclass
class NumberOeuvreByGenreDTO:
    genre: str
    number_oeuvre: int

    @classmethod
    def from_model(cls, genre, number_oeuvre):
        return cls(
            genre = genre,
            number_oeuvre = number_oeuvre
        )