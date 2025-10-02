from sqlmodel import SQLModel, Field

class Oeuvre(SQLModel, table=True):
    __tablename__ = "oeuvre"
    id_oeuvre: int | None = Field(default=None, primary_key=True)
    title: str
    description: str | None = Field(default=None)
    rating: int
    upc: str
    prix_ht: float
    taxe: float
    nb_available: int
    nb_review: int
    image_url: str
    genre_fk: int = Field(foreign_key="genre.id_genre")
    
    @classmethod
    def from_item(cls, item: dict, genre_id: int):
        return cls(
            title=item["title"],
            description=item["description"],
            rating=item["rating"],
            upc=item["upc"],
            prix_ht=item["prix_ht"],
            taxe=item["taxe"],
            nb_available=item["nb_available"],
            nb_review=item["nb_review"],
            image_url=item["image_url"],
            genre_fk=genre_id
        )