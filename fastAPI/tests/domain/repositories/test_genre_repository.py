import pytest
from app.domain.repositories.genre_repository import GenreRepository

@pytest.mark.asyncio
async def test_get_all_not_implemented():
    # On ne peut pas instancier directement un ABC avec abstractmethod
    with pytest.raises(TypeError):
        repo = GenreRepository()
