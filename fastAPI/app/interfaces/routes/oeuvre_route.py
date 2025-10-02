from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from app.core.database import get_session
from app.infrastructure.repositories.oeuvre_repository_impl import OeuvreRepositoryImpl
from app.application.service.oeuvre_service import OeuvreService
from app.interfaces.schemas.oeuvre_response import *

router = APIRouter(prefix="/oeuvre", tags=["Oeuvre"])

def get_oeuvre_service(session: AsyncSession = Depends(get_session)) -> OeuvreService:
    """
    Fournit une instance de OeuvreService avec le repository injecté.
    """
    repo = OeuvreRepositoryImpl(session)
    return OeuvreService(repo)

@router.get("/all", response_model=list[OeuvreResponse])
async def get_all_oeuvres(service: OeuvreService = Depends(get_oeuvre_service)):
    """
    Récupère toutes les oeuvres.

    Returns:
        List[OeuvreResponse]: Liste complète des oeuvres.
    """
    dtos = await service.list_all_oeuvres()
    return [OeuvreResponse.from_dto(dto) for dto in dtos]

@router.get("/upc/{upc}", response_model=list[OeuvreResponse])
async def get_oeuvres_by_upc(upc: str, service: OeuvreService = Depends(get_oeuvre_service)):
    """
    Récupère les oeuvres correspondant à un UPC donné.

    Args:
        upc (str): Le code UPC de l'oeuvre.

    Returns:
        List[OeuvreResponse]: Liste des oeuvres correspondantes.
    """
    dtos = await service.list_oeuvres_by_upc(upc)
    return [OeuvreResponse.from_dto(dto) for dto in dtos]

@router.get("/genre/{genre_name}", response_model=list[OeuvreResponse])
async def get_oeuvres_by_genre(genre_name: str, service: OeuvreService = Depends(get_oeuvre_service)):
    """
    Récupère les oeuvres d'un genre spécifique.

    Args:
        genre_name (str): Nom du genre.

    Returns:
        List[OeuvreResponse]: Liste des oeuvres du genre.
    """
    dtos = await service.list_by_genre(genre_name)
    return [OeuvreResponse.from_dto(dto) for dto in dtos]

@router.get("/prix/", response_model=list[OeuvreResponse])
async def get_oeuvres_by_price(min_value: float, max_value: float, service: OeuvreService = Depends(get_oeuvre_service)):
    """
    Récupère les oeuvres dont le prix TTC est compris entre min_value et max_value.

    Args:
        min_value (float): Prix minimum.
        max_value (float): Prix maximum.

    Returns:
        List[OeuvreResponse]: Liste des oeuvres filtrées par prix.
    """
    dtos = await service.list_by_price_between(min_value, max_value)
    return [OeuvreResponse.from_dto(dto) for dto in dtos]

@router.get("/stats/avg-price", response_model=list)
async def avg_price(service: OeuvreService = Depends(get_oeuvre_service)):
    """
    Récupère le prix moyen TTC des oeuvres par genre.

    Returns:
        List[PriceOeuvreByGenreResponse]: Liste des prix moyens par genre.
    """
    dtos = await service.avg_price_by_genre()
    return [PriceOeuvreByGenreResponse.from_dto(dto) for dto in dtos]

@router.get("/stats/count", response_model=list)
async def count_oeuvres(service: OeuvreService = Depends(get_oeuvre_service)):
    """
    Récupère le nombre d'oeuvres par genre.

    Returns:
        List[NumberOeuvreByGenreResponse]: Liste des nombres d'oeuvres par genre.
    """
    dtos = await service.count_by_genre()
    return [NumberOeuvreByGenreResponse.from_dto(dto) for dto in dtos]
