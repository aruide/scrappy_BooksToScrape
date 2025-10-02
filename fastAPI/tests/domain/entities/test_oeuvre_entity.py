import pytest
from app.domain.entities.oeuvre_entity import OeuvreEntity

# -------- FIXTURE --------
@pytest.fixture
def fake_oeuvre() -> OeuvreEntity:
    return OeuvreEntity(
        id_oeuvre=1,
        title="Inception",
        description="Un film de Christopher Nolan",
        rating=5,
        upc="123456789",
        prix_ht=10.0,
        taxe=2.0,
        nb_available=20,
        nb_review=100,
        image_url="http://example.com/inception.jpg",
        genre_fk=1
    )

# -------- TESTS --------
def test_create_oeuvre_entity(fake_oeuvre):
    assert fake_oeuvre.id_oeuvre == 1
    assert fake_oeuvre.title == "Inception"
    assert fake_oeuvre.description == "Un film de Christopher Nolan"
    assert fake_oeuvre.rating == 5
    assert fake_oeuvre.upc == "123456789"
    assert fake_oeuvre.prix_ht == 10.0
    assert fake_oeuvre.taxe == 2.0
    assert fake_oeuvre.nb_available == 20
    assert fake_oeuvre.nb_review == 100
    assert fake_oeuvre.image_url == "http://example.com/inception.jpg"
    assert fake_oeuvre.genre_fk == 1

def test_optional_fields():
    # Vérifie que l'on peut créer une entité avec id_oeuvre et description à None
    oeuvre = OeuvreEntity(
        id_oeuvre=None,
        title="Matrix",
        description=None,
        rating=4,
        upc="987654321",
        prix_ht=15.0,
        taxe=3.0,
        nb_available=10,
        nb_review=50,
        image_url="http://example.com/matrix.jpg",
        genre_fk=2
    )

    assert oeuvre.id_oeuvre is None
    assert oeuvre.description is None
    assert oeuvre.title == "Matrix"
    assert oeuvre.rating == 4
