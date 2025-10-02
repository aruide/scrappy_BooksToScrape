import pytest
from datetime import datetime
from app.infrastructure.db.exchange_rates import ExchangeRates

# ---------------- Test d'instanciation simple ----------------
def test_create_exchange_rate():
    rate = ExchangeRates(
        id_exchange_rate=1,
        base_currency="USD",
        target_currency="EUR",
        rate=0.95,
        retrieved_at=datetime(2025, 10, 2, 12, 0)
    )
    assert rate.base_currency == "USD"
    assert rate.target_currency == "EUR"
    assert rate.rate == 0.95
    assert rate.retrieved_at == datetime(2025, 10, 2, 12, 0)

# ---------------- Test valeur par défaut retrieved_at ----------------
def test_default_retrieved_at():
    rate = ExchangeRates(
        base_currency="USD",
        target_currency="EUR",
        rate=0.95
    )
    assert isinstance(rate.retrieved_at, datetime)

# ---------------- Test insertion / lecture en DB mémoire ----------------
def test_insert_and_read_exchange_rate(session):
    rate = ExchangeRates(
        base_currency="USD",
        target_currency="EUR",
        rate=0.95
    )

    session.add(rate)
    session.commit()
    session.refresh(rate)

    result = session.query(ExchangeRates).first()
    assert result.base_currency == "USD"
    assert result.rate == 0.95
    assert result.id_exchange_rate is not None
