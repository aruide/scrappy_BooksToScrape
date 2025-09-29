from sqlmodel import SQLModel, Field, Session, select, create_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from app.model.genre.genre import Genre

async def get_all_genre(session: AsyncSession):
    statement = select(Genre.name)
    result = await session.exec(statement)
    return [g for g in result.all()]
