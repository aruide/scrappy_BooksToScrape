from typing import List
from app.domain.entities.oeuvre_entity import OeuvreEntity
from app.domain.repositories.oeuvre_repository import OeuvreRepository

class OeuvreService:
    """
    Service pour gérer les opérations liées aux œuvres.
    """

    def __init__(self, repository: OeuvreRepository):
        """
        Initialise le service avec un repository d'œuvres.

        Args:
            repository (OeuvreRepository): Le repository pour accéder aux œuvres.
        """
        self.repository = repository

    async def list_all_oeuvres(self) -> List[OeuvreEntity]:
        """
        Récupère toutes les œuvres.

        Returns:
            List[OeuvreEntity]: Liste de toutes les œuvres.
        """
        return await self.repository.get_all()
    
    async def list_oeuvres_by_upc(self, upc: str) -> List[OeuvreEntity]:
        """
        Récupère les œuvres correspondant à un UPC donné.

        Args:
            upc (str): Le code UPC de l'œuvre.

        Returns:
            List[OeuvreEntity]: Liste des œuvres correspondantes.
        """
        return await self.repository.get_oeuvres_by_upc(upc)

    async def list_by_genre(self, genre: str) -> List[OeuvreEntity]:
        """
        Récupère les œuvres d'un genre spécifique.

        Args:
            genre (str): Nom du genre.

        Returns:
            List[OeuvreEntity]: Liste des œuvres correspondant au genre.
        """
        return await self.repository.get_by_genre(genre)

    async def list_by_price_between(self, min_value: float, max_value: float) -> List[OeuvreEntity]:
        """
        Récupère les œuvres dont le prix TTC est compris entre deux valeurs.

        Args:
            min_value (float): Prix minimum.
            max_value (float): Prix maximum.

        Returns:
            List[OeuvreEntity]: Liste des œuvres correspondant aux critères.
        """
        return await self.repository.get_between_prices(min_value, max_value)

    async def avg_price_by_genre(self):
        """
        Calcule le prix moyen TTC des œuvres par genre.

        Returns:
            List: Liste des prix moyens par genre.
        """
        return await self.repository.get_avg_price_by_genre()

    async def count_by_genre(self):
        """
        Compte le nombre d'œuvres par genre.

        Returns:
            List: Liste du nombre d'œuvres par genre.
        """
        return await self.repository.get_number_by_genre()
