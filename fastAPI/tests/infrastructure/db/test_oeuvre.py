def test_create_oeuvre(fake_oeuvre, fake_genre):
    # fake_oeuvre vient directement du conftest
    assert fake_oeuvre.title == "Inception"
    assert fake_oeuvre.genre_fk == fake_genre.id_genre

def test_insert_and_read_oeuvre(session, fake_genre):
    # session et fake_genre viennent du conftest
    from app.infrastructure.db.oeuvre import Oeuvre

    oeuvre = Oeuvre(
        title="Matrix",
        description="Film de Wachowski",
        rating=4,
        upc="987654",
        prix_ht=15.0,
        taxe=3.0,
        nb_available=10,
        nb_review=50,
        image_url="http://example.com/matrix.jpg",
        genre_fk=fake_genre.id_genre
    )

    session.add(oeuvre)
    session.commit()
    session.refresh(oeuvre)

    result = session.query(Oeuvre).first()
    assert result.title == "Inception"
