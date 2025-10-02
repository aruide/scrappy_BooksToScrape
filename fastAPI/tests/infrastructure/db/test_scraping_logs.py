import pytest
from datetime import datetime
from app.infrastructure.db.scraping_logs import ScrapingLogs
from app.infrastructure.db.exchange_rates import ExchangeRates

# ---------------- Fixture pour un exchange_rate ----------------
@pytest.fixture
def fake_exchange_rate(session):
    # NE PAS mettre id_exchange_rate=6
    rate = ExchangeRates(base_currency="USD", target_currency="EUR", rate=0.95)
    session.add(rate)
    session.commit()
    session.refresh(rate)  # récupère l’ID généré par SQLite
    return rate

# ---------------- Test d'instanciation simple ----------------
def test_create_scraping_log(fake_exchange_rate):
    log = ScrapingLogs(
        site_url="http://example.com",
        exchange_rate_fk=fake_exchange_rate.id_exchange_rate,
        scraped_at=datetime(2025, 10, 2, 14, 0)  # facultatif
    )
    assert log.site_url == "http://example.com"
    assert log.exchange_rate_fk == fake_exchange_rate.id_exchange_rate

# ---------------- Test valeur par défaut scraped_at ----------------
def test_default_scraped_at(fake_exchange_rate):
    log = ScrapingLogs(
        site_url="http://example.com",
        exchange_rate_fk=fake_exchange_rate.id_exchange_rate
    )
    assert isinstance(log.scraped_at, datetime)

# ---------------- Test insertion / lecture en DB mémoire ----------------
def test_insert_and_read_scraping_log(session, fake_exchange_rate):
    log = ScrapingLogs(
        site_url="http://example.com",
        exchange_rate_fk=fake_exchange_rate.id_exchange_rate
    )
    session.add(log)
    session.commit()
    session.refresh(log)

    result = session.query(ScrapingLogs).first()
    assert result.site_url == "http://example.com"
    assert result.id_scraping_log is not None
    # Comparaison avec l'ID réel généré par SQLite
    #assert result.exchange_rate_fk == fake_exchange_rate.id_exchange_rate
