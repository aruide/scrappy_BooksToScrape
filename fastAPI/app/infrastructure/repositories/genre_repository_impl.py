from sqlmodel import select
from typing import List
from sqlalchemy import func
from sqlmodel.ext.asyncio.session import AsyncSession

from app.domain.repositories.genre_repository import GenreRepository
from app.infrastructure.db.genre import Genre

class GenreRepositoryImpl(GenreRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def get_all(self) -> List:
        statement = select(Genre.name)
        result = await self.session.exec(statement)
        return [name for name in result.all()]