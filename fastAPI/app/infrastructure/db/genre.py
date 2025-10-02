from sqlmodel import SQLModel, Field

class Genre(SQLModel, table=True):
    """
    Modèle représentant un genre.

    Attributes:
        id_genre (int | None): Identifiant unique du genre.
        name (str): Nom du genre.
    """

    __tablename__ = "genre"

    id_genre: int | None = Field(default=None, primary_key=True)
    name: str

    @classmethod
    def from_item(cls, item: dict):
        """
        Crée une instance de Genre à partir d'un dictionnaire.

        Args:
            item (dict): Dictionnaire contenant au moins la clé 'name'.

        Returns:
            Genre: Nouvelle instance du genre.
        """
        return cls(name=item["name"])
