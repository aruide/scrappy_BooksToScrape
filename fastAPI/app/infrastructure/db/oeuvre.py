from sqlmodel import SQLModel, Field

class Oeuvre(SQLModel, table=True):
    """
    Modèle représentant une oeuvre (livre, film, etc.).

    Attributes:
        id_oeuvre (int | None): Identifiant unique de l'oeuvre.
        title (str): Titre de l'oeuvre.
        description (str | None): Description de l'oeuvre.
        rating (int): Note ou évaluation de l'oeuvre.
        upc (str): Code UPC de l'oeuvre.
        prix_ht (float): Prix hors taxe.
        taxe (float): Taux de taxe appliqué au prix.
        nb_available (int): Nombre d'exemplaires disponibles.
        nb_review (int): Nombre de critiques.
        image_url (str): URL de l'image de l'oeuvre.
        genre_fk (int): Identifiant du genre associé (clé étrangère vers Genre).
    """

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
        """
        Crée une instance de Oeuvre à partir d'un dictionnaire et d'un ID de genre.

        Args:
            item (dict): Dictionnaire contenant les données de l'oeuvre.
            genre_id (int): Identifiant du genre associé à l'oeuvre.

        Returns:
            Oeuvre: Nouvelle instance du modèle Oeuvre.
        """
        return cls(
            title=item["title"],
            description=item.get("description"),
            rating=item["rating"],
            upc=item["upc"],
            prix_ht=item["prix_ht"],
            taxe=item["taxe"],
            nb_available=item["nb_available"],
            nb_review=item["nb_review"],
            image_url=item["image_url"],
            genre_fk=genre_id,
        )
