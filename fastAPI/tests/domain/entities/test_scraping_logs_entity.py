import pytest
from datetime import datetime
from app.domain.entities.scraping_logs_entity import ScrapingLogsEntity

# -------- FIXTURE --------
@pytest.fixture
def fake_scraping_log() -> ScrapingLogsEntity:
    return ScrapingLogsEntity(
        id_scraping_log=1,
        scraped_at=datetime(2025, 10, 2, 14, 30, 0),
        site_url="http://example.com",
        exchange_rate_fk=1
    )

# -------- TESTS --------
def test_create_scraping_log_entity(fake_scraping_log):
    assert fake_scraping_log.id_scraping_log == 1
    assert fake_scraping_log.site_url == "http://example.com"
    assert fake_scraping_log.exchange_rate_fk == 1
    assert fake_scraping_log.scraped_at == datetime(2025, 10, 2, 14, 30, 0)

def test_optional_fields_scraping_log():
    log = ScrapingLogsEntity(
        id_scraping_log=None,
        scraped_at=datetime.now(),
        site_url="http://test.com",
        exchange_rate_fk=None
    )
    assert log.id_scraping_log is None
    assert log.exchange_rate_fk is None
    assert log.site_url == "http://test.com"
    assert isinstance(log.scraped_at, datetime)
