import pytest
from unittest.mock import AsyncMock

from app.application.service.genre_service import GenreService

@pytest.mark.asyncio
async def test_list_all_genre():
    # Arrange : on simule des genres
    fake_genres = ["Drama", "Comedy", "Sci-Fi"]
    mock_repo = AsyncMock()
    mock_repo.get_all.return_value = fake_genres

    service = GenreService(mock_repo)

    # Act
    result = await service.list_all_genre()

    # Assert
    assert len(result) == 3
    assert "Drama" in result
    mock_repo.get_all.assert_called_once()
