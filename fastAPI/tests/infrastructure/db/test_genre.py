import pytest
from app.infrastructure.db.genre import Genre

# ---------------- Test d'instanciation simple ----------------
def test_create_genre():
    genre = Genre(id_genre=1, name="Sci-Fi")
    assert genre.id_genre == 1
    assert genre.name == "Sci-Fi"

# ---------------- Test de la méthode from_item ----------------
def test_from_item_method():
    item = {"name": "Fantasy"}
    genre = Genre.from_item(item)
    assert genre.name == "Fantasy"
    assert genre.id_genre is None  # id non défini par from_item

# ---------------- Test insertion / lecture en DB mémoire ----------------
def test_insert_and_read_genre(session):
    genre = Genre(name="Horror")  # id auto-généré
    session.add(genre)
    session.commit()
    session.refresh(genre)

    # Lecture
    result = session.query(Genre).first()
    assert result.name == "Horror"
    assert result.id_genre is not None
