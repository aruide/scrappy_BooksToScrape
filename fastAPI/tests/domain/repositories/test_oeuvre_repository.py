import pytest
from app.domain.repositories.oeuvre_repository import OeuvreRepository
from app.domain.dto.oeuvre_response import OeuvreDTO

@pytest.mark.asyncio
async def test_get_all_not_implemented():
    repo = OeuvreRepository()
    with pytest.raises(NotImplementedError):
        await repo.get_all()

@pytest.mark.asyncio
async def test_get_oeuvres_by_upc_not_implemented():
    repo = OeuvreRepository()
    with pytest.raises(NotImplementedError):
        await repo.get_oeuvres_by_upc("123456")

@pytest.mark.asyncio
async def test_get_by_genre_not_implemented():
    repo = OeuvreRepository()
    with pytest.raises(NotImplementedError):
        await repo.get_by_genre("Sci-Fi")

@pytest.mark.asyncio
async def test_get_between_prices_not_implemented():
    repo = OeuvreRepository()
    with pytest.raises(NotImplementedError):
        await repo.get_between_prices(5.0, 15.0)

@pytest.mark.asyncio
async def test_get_avg_price_by_genre_not_implemented():
    repo = OeuvreRepository()
    with pytest.raises(NotImplementedError):
        await repo.get_avg_price_by_genre()

@pytest.mark.asyncio
async def test_get_number_by_genre_not_implemented():
    repo = OeuvreRepository()
    with pytest.raises(NotImplementedError):
        await repo.get_number_by_genre()
