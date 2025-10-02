import pytest
from app.domain.entities.oeuvre_scraping_entity import OeuvreScrapingEntity

# -------- FIXTURE --------
@pytest.fixture
def fake_oeuvre_scraping() -> OeuvreScrapingEntity:
    return OeuvreScrapingEntity(
        oeuvre_fk=1,
        scraping_log_fk=2
    )

# -------- TESTS --------
def test_create_oeuvre_scraping_entity(fake_oeuvre_scraping):
    assert fake_oeuvre_scraping.oeuvre_fk == 1
    assert fake_oeuvre_scraping.scraping_log_fk == 2

def test_oeuvre_scraping_entity_values():
    entity = OeuvreScrapingEntity(oeuvre_fk=10, scraping_log_fk=20)
    assert entity.oeuvre_fk == 10
    assert entity.scraping_log_fk == 20
