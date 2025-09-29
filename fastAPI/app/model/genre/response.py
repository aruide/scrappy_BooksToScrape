from pydantic import BaseModel

class GenreResponse(BaseModel):
    id_genre: int
    name: str
    
    model_config = {"from_attributes": True}