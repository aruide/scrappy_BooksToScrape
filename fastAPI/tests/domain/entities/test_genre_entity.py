import pytest
from app.domain.entities.genre_entity import GenreEntity

# -------- FIXTURE --------
@pytest.fixture
def fake_genre() -> GenreEntity:
    return GenreEntity(
        id_genre=1,
        name="Science Fiction"
    )

# -------- TESTS --------
def test_create_genre_entity(fake_genre):
    assert fake_genre.id_genre == 1
    assert fake_genre.name == "Science Fiction"

def test_optional_id_genre():
    # Vérifie que id_genre peut être None
    genre = GenreEntity(
        id_genre=None,
        name="Comedy"
    )
    assert genre.id_genre is None
    assert genre.name == "Comedy"
