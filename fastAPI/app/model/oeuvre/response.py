from pydantic import BaseModel, computed_field
from app.utils.exchange import exchange

class OeuvreResponse(BaseModel):
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
    
    @computed_field
    @property
    def prix_ttc(self) -> float:
        return self.prix_ht * (1 + self.taxe)
        
    @computed_field
    @property
    def prix_euro(self) -> float:
        return exchange.exchange_livre_to_euro(self.prix_ttc)
    
    model_config = {"from_attributes": True}
    
class PriceOeuvreByGenreResponse(BaseModel):
    genre: str
    prix_ttc_avg: float
    
    @computed_field
    @property
    def prix_ttc_avg_euro(self) -> float:
        return exchange.exchange_livre_to_euro(self.prix_ttc_avg)
        
class NumberOeuvreByGenreResponse(BaseModel):
    genre: str
    number_oeuvre: float