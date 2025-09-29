from sqlmodel import select
from sqlalchemy import func
from sqlmodel.ext.asyncio.session import AsyncSession
from app.model.oeuvre.oeuvre import Oeuvre
from app.model.oeuvre.response import *
from app.model.genre.genre import Genre
from app.model.oeuvre.response import *

async def get_all_oeuvre(session: AsyncSession) -> OeuvreResponse:
    statement = (select(Oeuvre, Genre.name.label("genre"))
                 .join(Genre)
                 )
    result = await session.exec(statement)
    return [OeuvreResponse(**oeuvre.__dict__, genre = genre_name) for oeuvre, genre_name in result.all()]

async def get_oeuvre_by_genre(session: AsyncSession, genre_name: str) -> OeuvreResponse:
    statement = ( select(Oeuvre, Genre.name.label("genre"))
                  .join(Genre)
                  .where(Genre.name == genre_name)
                )
    result = await session.exec(statement)
    return [OeuvreResponse(**oeuvre.__dict__, genre = genre_name) for oeuvre, genre_name in result.all()]

async def get_oeuvre_between(session: AsyncSession, min_value: float, max_value: float) -> OeuvreResponse:
    statement = ( select(Oeuvre, Genre.name.label("genre"))
                  .join(Genre)
                  .where((Oeuvre.prix_ht * (1 + Oeuvre.taxe))
                  .between(min_value, max_value)) 
                )
    result = await session.exec(statement)
    return [OeuvreResponse(**oeuvre.__dict__, genre = genre_name) for oeuvre, genre_name in result.all()]

async def get_avg_price_by_genre(session: AsyncSession):
    
    prix_ttc = func.avg(Oeuvre.prix_ht * (1 + Oeuvre.taxe)).label("prix_ttc")
    
    statement = ( select(Genre.name, prix_ttc)
                  .join(Oeuvre)
                  .group_by(Genre.name)
                  .order_by(prix_ttc.desc())
                )
    result = await session.exec(statement)
    return [PriceOeuvreByGenreResponse(genre= g[0], prix_ttc_avg= g[1]) for g in result.all()]

async def get_number_oeuvre_by_genre(session: AsyncSession):
    
    nb_oeuvre = func.count(Oeuvre.id_oeuvre).label("nb_oeuvre")
    
    statement = ( select(Genre.name, nb_oeuvre)
                  .join(Oeuvre)
                  .group_by(Genre.name)
                  .order_by(nb_oeuvre.desc())
                )
    result = await session.exec(statement)
    return [NumberOeuvreByGenreResponse(genre= g[0], number_oeuvre= g[1]) for g in result.all()]