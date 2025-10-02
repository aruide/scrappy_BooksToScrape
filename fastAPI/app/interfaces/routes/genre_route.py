from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from app.core.database import get_session
from app.infrastructure.repositories.genre_repository_impl import GenreRepositoryImpl
from app.application.service.genre_service import GenreService

router = APIRouter(prefix="/genre", tags=["Genre"])

def get_genre_service(session: AsyncSession = Depends(get_session)) -> GenreService:
    repo = GenreRepositoryImpl(session)
    return GenreService(repo)

@router.get("/all")
async def get_all_genres(service: GenreService = Depends(get_genre_service)):
    return await service.list_all_genre()