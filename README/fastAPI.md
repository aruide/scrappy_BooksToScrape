# FastAPI

## Structure du dossier FastAPI

```bash
│
├── application/                 # Couche "service" (logique métier)
│       └── service/
│              ├── genre_service.py        # Gère les opérations liées aux genres
│              └── oeuvre_service.py       # Gère les opérations liées aux œuvres
│
├── core/                        # Configurations techniques
│    └── database.py             # Connexion et gestion de la base de données
│
├── domain/                      # Couche "métier" (entités, DTO, repositories)
│    ├── dto/
│    │    └── oeuvre_response.py # Objets de transfert de données (DTO)
│    ├── entities/
│    │    ├── exchange_rates_entity.py
│    │    ├── genre_entity.py
│    │    ├── oeuvre_entity.py
│    │    ├── oeuvre_scraping_entity.py
│    │    └── scraping_logs_entity.py
│    └── repositories/           # Interfaces des dépôts
│         ├── genre_repository.py
│         └── oeuvre_repository.py
│
├── infrastructure/              # Implémentations concrètes
│    ├── db/                     # Modèles liés à la base de données
│    │    ├── exchange_rates.py
│    │    ├── genre.py
│    │    ├── oeuvre.py
│    │    ├── oeuvre_scraping.py
│    │    └── scraping_logs.py
│    └── repositories/           # Implémentations des repositories
│         ├── genre_repository_impl.py
│         └── oeuvre_repository_impl.py
│
├── interfaces/                  # Couche d'abstraction (API, DB, etc.)
│    ├── db/                     # Interfaces DB si nécessaires
│    └── repositories/           # Interfaces des dépôts
│
└── main.py                      # Point d’entrée de l’application FastAPI

```


## Commande pour FastAPI

1) *pour lancer le serveur*

```bash
# se rendre dans le dossier fastAPI
cd fastAPI

# lancer le serveur
uvicorn main:app --reload
```

## URL

URL de base: http://localhost:8000 \
URL de swagger: http://localhost:8000/docs