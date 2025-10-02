from typing import List
from app.domain.dto.oeuvre_response import OeuvreDTO, PriceOeuvreByGenreDTO, NumberOeuvreByGenreDTO

class OeuvreRepository:
    """
    Interface abstraite pour le repository des œuvres.
    Définit les opérations disponibles pour manipuler les œuvres.
    """

    async def get_all(self) -> List[OeuvreDTO]:
        """
        Récupère toutes les œuvres.

        Returns:
            List[OeuvreDTO]: Liste de toutes les œuvres.
        """
        raise NotImplementedError
    
    async def get_oeuvres_by_upc(self, upc: str) -> List[OeuvreDTO]:
        """
        Récupère les œuvres correspondant à un code UPC donné.

        Args:
            upc (str): Code UPC à rechercher.

        Returns:
            List[OeuvreDTO]: Liste des œuvres correspondantes.
        """
        raise NotImplementedError

    async def get_by_genre(self, genre: str) -> List[OeuvreDTO]:
        """
        Récupère les œuvres appartenant à un genre spécifique.

        Args:
            genre (str): Nom du genre.

        Returns:
            List[OeuvreDTO]: Liste des œuvres du genre.
        """
        raise NotImplementedError

    async def get_between_prices(self, min_value: float, max_value: float) -> List[OeuvreDTO]:
        """
        Récupère les œuvres dont le prix TTC est compris entre deux valeurs.

        Args:
            min_value (float): Prix minimum.
            max_value (float): Prix maximum.

        Returns:
            List[OeuvreDTO]: Liste des œuvres filtrées par prix.
        """
        raise NotImplementedError

    async def get_avg_price_by_genre(self) -> List[PriceOeuvreByGenreDTO]:
        """
        Calcule le prix moyen TTC des œuvres par genre.

        Returns:
            List[PriceOeuvreByGenreDTO]: Liste des genres avec leur prix moyen.
        """
        raise NotImplementedError

    async def get_number_by_genre(self) -> List[NumberOeuvreByGenreDTO]:
        """
        Compte le nombre d'œuvres par genre.

        Returns:
            List[NumberOeuvreByGenreDTO]: Liste des genres avec leur nombre d'œuvres.
        """
        raise NotImplementedError
