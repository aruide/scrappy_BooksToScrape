import pytest
from datetime import datetime
from sqlmodel import SQLModel, create_engine, Session
from app.infrastructure.db.oeuvre import Oeuvre
from app.infrastructure.db.genre import Genre
from app.infrastructure.db.exchange_rates import ExchangeRates
from app.infrastructure.db.scraping_logs import ScrapingLogs
from app.infrastructure.db.oeuvre_scraping import OeuvreScraping

# ----------------- Fixture globale pour la DB -----------------
@pytest.fixture(scope="session")
def test_engine():
    """
    Crée un engine SQLite en mémoire pour tous les tests du module.
    Les tables sont créées automatiquement pour toutes les entités.
    """
    engine = create_engine("sqlite:///:memory:", echo=False)
    SQLModel.metadata.create_all(engine)
    yield engine
    # SQLite en mémoire disparaît à la fin de la session

# ----------------- Fixture session pour chaque test -----------------
@pytest.fixture
def session(test_engine):
    """
    Fournit une session SQLModel isolée pour chaque test.
    Les modifications sont annulées après le test grâce au rollback.
    """
    with Session(test_engine) as session:
        yield session
        session.rollback()

# ----------------- Fixtures helpers pour insérer des données -----------------

@pytest.fixture
def fake_genre(session):
    genre = Genre(name="Sci-Fi")
    session.add(genre)
    session.commit()
    session.refresh(genre)
    return genre

@pytest.fixture
def fake_oeuvre(session, fake_genre):
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
        genre_fk=fake_genre.id_genre
    )
    session.add(oeuvre)
    session.commit()
    session.refresh(oeuvre)
    return oeuvre

@pytest.fixture
def fake_exchange_rate(session):
    rate = ExchangeRates(
        base_currency="USD",
        target_currency="EUR",
        rate=0.95,
        retrieved_at=datetime(2025, 10, 2, 12, 0)
    )
    session.add(rate)
    session.commit()
    session.refresh(rate)
    return rate

@pytest.fixture
def fake_scraping_log(session, fake_exchange_rate):
    log = ScrapingLogs(
        site_url="http://example.com",
        scraped_at=datetime(2025, 10, 2, 14, 0),
        exchange_rate_fk=fake_exchange_rate.id_exchange_rate
    )
    session.add(log)
    session.commit()
    session.refresh(log)
    return log

@pytest.fixture
def fake_oeuvre_scraping(session, fake_oeuvre, fake_scraping_log):
    oeuv_scraping = OeuvreScraping(
        oeuvre_fk=fake_oeuvre.id_oeuvre,
        scraping_log_fk=fake_scraping_log.id_scraping_log
    )
    session.add(oeuv_scraping)
    session.commit()
    session.refresh(oeuv_scraping)
    return oeuv_scraping
