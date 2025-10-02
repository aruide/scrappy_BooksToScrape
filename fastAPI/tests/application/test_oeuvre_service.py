import pytest
from unittest.mock import AsyncMock

from app.application.service.oeuvre_service import OeuvreService
from app.domain.entities.oeuvre_entity import OeuvreEntity


# -------- FIXTURE POUR SIMPLIFIER LES TESTS --------
@pytest.fixture
def fake_oeuvre() -> OeuvreEntity:
    return OeuvreEntity(
        id_oeuvre=1,
        title="Inception",
        description="Un film de Christopher Nolan",
        rating=5,
        upc="123456",
        prix_ht=10.0,
        taxe=2.0,
        nb_available=20,
        nb_review=100,
        image_url="http://example.com/inception.jpg",
        genre_fk=1,
    )


# -------- TESTS --------
@pytest.mark.asyncio
async def test_list_all_oeuvres(fake_oeuvre):
    mock_repo = AsyncMock()
    mock_repo.get_all.return_value = [fake_oeuvre]

    service = OeuvreService(mock_repo)
    result = await service.list_all_oeuvres()

    assert len(result) == 1
    assert result[0].title == "Inception"
    assert result[0].id_oeuvre == 1
    mock_repo.get_all.assert_called_once()


@pytest.mark.asyncio
async def test_list_oeuvres_by_upc(fake_oeuvre):
    mock_repo = AsyncMock()
    mock_repo.get_oeuvres_by_upc.return_value = [fake_oeuvre]

    service = OeuvreService(mock_repo)
    result = await service.list_oeuvres_by_upc("123456")

    assert result[0].upc == "123456"
    assert result[0].title == "Inception"
    mock_repo.get_oeuvres_by_upc.assert_called_once_with("123456")


@pytest.mark.asyncio
async def test_list_by_genre(fake_oeuvre):
    mock_repo = AsyncMock()
    mock_repo.get_by_genre.return_value = [fake_oeuvre]

    service = OeuvreService(mock_repo)
    result = await service.list_by_genre("Sci-Fi")

    assert result[0].genre_fk == 1
    assert result[0].title == "Inception"
    mock_repo.get_by_genre.assert_called_once_with("Sci-Fi")


@pytest.mark.asyncio
async def test_list_by_price_between(fake_oeuvre):
    mock_repo = AsyncMock()
    mock_repo.get_between_prices.return_value = [fake_oeuvre]

    service = OeuvreService(mock_repo)
    result = await service.list_by_price_between(5.0, 15.0)

    assert 5.0 <= result[0].prix_ht <= 15.0
    assert result[0].title == "Inception"
    mock_repo.get_between_prices.assert_called_once_with(5.0, 15.0)


@pytest.mark.asyncio
async def test_avg_price_by_genre():
    fake_avg = {"Sci-Fi": 12.5}
    mock_repo = AsyncMock()
    mock_repo.get_avg_price_by_genre.return_value = fake_avg

    service = OeuvreService(mock_repo)
    result = await service.avg_price_by_genre()

    assert result["Sci-Fi"] == 12.5
    mock_repo.get_avg_price_by_genre.assert_called_once()


@pytest.mark.asyncio
async def test_count_by_genre():
    fake_counts = {"Drama": 5, "Comedy": 3}
    mock_repo = AsyncMock()
    mock_repo.get_number_by_genre.return_value = fake_counts

    service = OeuvreService(mock_repo)
    result = await service.count_by_genre()

    assert result["Drama"] == 5
    assert result["Comedy"] == 3
    mock_repo.get_number_by_genre.assert_called_once()
