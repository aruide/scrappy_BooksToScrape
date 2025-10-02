# Tests - FastAPI / SQLModel Project

Ce dossier contient les tests unitaires et d’intégration pour le projet.

Les tests couvrent :

- Application Layer : OeuvreService, GenreService
- Domain Layer : Entités (OeuvreEntity, GenreEntity, etc.)
- Infrastructure Layer : Modèles SQLModel (Oeuvre, Genre, ExchangeRates, ScrapingLogs, OeuvreScraping)

## Structure du dossier tests

```bash
tests/
├── application/           # Tests des services (OeuvreService, GenreService)
├── domain/                # Tests des entités et DTO
├── infrastructure/
│    └── db/               # Tests des modèles SQLModel
└── conftest.py            # Fixtures globales pour la DB et données de test

```

## Commande pour les tests

## Commande pour FastAPI

1) *pour lancer les tests*

```bash
pytest -v
```