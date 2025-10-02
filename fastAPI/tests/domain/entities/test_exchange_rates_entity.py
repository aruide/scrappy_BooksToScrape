import pytest
from datetime import datetime
from app.domain.entities.exchange_rates_entity import ExchangeRatesEntity

# -------- FIXTURE --------
@pytest.fixture
def fake_exchange_rate() -> ExchangeRatesEntity:
    return ExchangeRatesEntity(
        id_exchange_rate=1,
        base_currency="USD",
        target_currency="EUR",
        rate=0.95,
        retrieved_at=datetime(2025, 10, 2, 12, 0, 0)
    )

# -------- TESTS --------
def test_create_exchange_rate_entity(fake_exchange_rate):
    assert fake_exchange_rate.id_exchange_rate == 1
    assert fake_exchange_rate.base_currency == "USD"
    assert fake_exchange_rate.target_currency == "EUR"
    assert fake_exchange_rate.rate == 0.95
    assert fake_exchange_rate.retrieved_at == datetime(2025, 10, 2, 12, 0, 0)

def test_optional_id_exchange_rate():
    entity = ExchangeRatesEntity(
        id_exchange_rate=None,
        base_currency="GBP",
        target_currency="USD",
        rate=1.25,
        retrieved_at=datetime.now()
    )
    assert entity.id_exchange_rate is None
    assert entity.base_currency == "GBP"
    assert entity.target_currency == "USD"
    assert entity.rate == 1.25
    assert isinstance(entity.retrieved_at, datetime)
