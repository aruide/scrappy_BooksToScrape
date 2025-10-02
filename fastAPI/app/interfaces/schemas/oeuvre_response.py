from pydantic import BaseModel, computed_field
from datetime import datetime

class OeuvreResponse(BaseModel):
    """
    Représentation Pydantic d'une œuvre pour la réponse API.
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
    
    @computed_field
    @property
    def prix_ttc(self) -> float:
        """Calcule le prix TTC de l'œuvre."""
        return self.prix_ht * (1 + self.taxe)
        
    @computed_field
    @property
    def prix_ttc_euro(self) -> float:
        """Calcule le prix TTC en euros selon le taux de change."""
        return self.prix_ttc * self.exchange_eur
    
    @classmethod
    def from_dto(cls, dto):
        """Crée une instance à partir d'un DTO."""
        return cls(**dto.__dict__)
    
    model_config = {"from_attributes": True}


class PriceOeuvreByGenreResponse(BaseModel):
    """
    DTO pour le prix moyen TTC des œuvres par genre.
    """
    genre: str
    prix_ttc_avg: float
    exchange_eur: float
    
    @computed_field
    @property
    def prix_ttc_avg_euro(self) -> float:
        """Calcule le prix moyen TTC en euros selon le taux de change."""
        return self.prix_ttc_avg * self.exchange_eur
    
    @classmethod
    def from_dto(cls, dto):
        """Crée une instance à partir d'un DTO."""
        return cls(**dto.__dict__)


class NumberOeuvreByGenreResponse(BaseModel):
    """
    DTO pour le nombre d'œuvres par genre.
    """
    genre: str
    number_oeuvre: float
    
    @classmethod
    def from_dto(cls, dto):
        """Crée une instance à partir d'un DTO."""
        return cls(**dto.__dict__)
