from sqlmodel import SQLModel, Field

# Définition du modèle SQLModel
class Genre(SQLModel, table=True):
    __tablename__ = "genre"
    id_genre: int | None = Field(default=None, primary_key=True)
    name: str
    
    @classmethod
    def from_item(cls, item: dict):
        return cls(name=item["name"])