import pytest
from app.infrastructure.db.oeuvre_scraping import OeuvreScraping
from app.infrastructure.db.oeuvre import Oeuvre
from app.infrastructure.db.scraping_logs import ScrapingLogs


# ---------------- Fixtures dépendantes ----------------
@pytest.fixture
def fake_oeuvre(session):
    from app.infrastructure.db.genre import Genre
    # Crée un genre pour la FK
    genre = Genre(name="Sci-Fi")
    session.add(genre)
    session.commit()
    session.refresh(genre)

    oeuvre = Oeuvre(
        title="Inception",
        description="Film de Nolan",
        rating=5,
        upc="123456",
        prix_ht=10.0,
        taxe=2.0,
        nb_available=20,
        nb_review=100,
        image_url="http://example.com/inception.jpg",
        genre_fk=genre.id_genre
    )
    session.add(oeuvre)
    session.commit()
    session.refresh(oeuvre)
    return oeuvre

@pytest.fixture
def fake_scraping_log(session):
    from app.infrastructure.db.exchange_rates import ExchangeRates
    from app.infrastructure.db.scraping_logs import ScrapingLogs
    # Crée un exchange_rate pour la FK
    rate = ExchangeRates(base_currency="USD", target_currency="EUR", rate=0.95)
    session.add(rate)
    session.commit()
    session.refresh(rate)

    log = ScrapingLogs(
        site_url="http://example.com",
        exchange_rate_fk=rate.id_exchange_rate
    )
    session.add(log)
    session.commit()
    session.refresh(log)
    return log

# ---------------- Test instanciation ----------------
def test_create_oeuvre_scraping(fake_oeuvre, fake_scraping_log):
    oeuv_scraping = OeuvreScraping(
        oeuvre_fk=fake_oeuvre.id_oeuvre,
        scraping_log_fk=fake_scraping_log.id_scraping_log
    )
    assert oeuv_scraping.oeuvre_fk == fake_oeuvre.id_oeuvre
    assert oeuv_scraping.scraping_log_fk == fake_scraping_log.id_scraping_log

# ---------------- Test insertion / lecture DB ----------------
def test_insert_and_read_oeuvre_scraping(session, fake_oeuvre, fake_scraping_log):
    oeuv_scraping = OeuvreScraping(
        oeuvre_fk=fake_oeuvre.id_oeuvre,
        scraping_log_fk=fake_scraping_log.id_scraping_log
    )
    session.add(oeuv_scraping)
    session.commit()
    session.refresh(oeuv_scraping)

    result = session.query(OeuvreScraping).first()
    assert result.oeuvre_fk == fake_oeuvre.id_oeuvre
    assert result.scraping_log_fk == fake_scraping_log.id_scraping_log
