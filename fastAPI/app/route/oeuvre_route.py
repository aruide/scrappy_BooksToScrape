from fastapi import APIRouter, status, Depends, Query

from app.service.oeuvre_service import *
from app.core.database import database

router = APIRouter(prefix="/oeuvre", tags=["Oeuvre"])

@router.get("/all", status_code=status.HTTP_200_OK)
async def all(session = Depends(database.get_session)):
    return await get_all_oeuvre(session)

@router.get("/by_genre", status_code=status.HTTP_200_OK)
async def by_genre(session = Depends(database.get_session), 
                   genre_name: str = Query(..., description= "Nom du genre à filtrer")):
    return await get_oeuvre_by_genre(session, genre_name)

@router.get("/between", status_code=status.HTTP_200_OK)
async def between(session = Depends(database.get_session), 
                   min_value: float = Query(..., description= "valeur minimum du prix"),
                   max_value: float = Query(..., description= "valeur maximum du prix")):
    return await get_oeuvre_between(session, min_value, max_value)

@router.get("/price_by_genre", status_code=status.HTTP_200_OK)
async def price_by_genre(session = Depends(database.get_session)):
    return await get_avg_price_by_genre(session)

@router.get("/number_oeuvre_by_genre", status_code=status.HTTP_200_OK)
async def number_oeuvre_by_genre(session = Depends(database.get_session)):
    return await get_number_oeuvre_by_genre(session)