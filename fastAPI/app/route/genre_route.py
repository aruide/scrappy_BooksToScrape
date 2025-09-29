from fastapi import APIRouter, status, Depends

from app.service.genre_service import *
from app.core.database import database

router = APIRouter(prefix="/genre", tags=["Genre"])

@router.get("/list", status_code=status.HTTP_200_OK)
async def create_favorite(session = Depends(database.get_session)):
    return await get_all_genre(session)