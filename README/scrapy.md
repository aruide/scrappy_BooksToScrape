# Scrapy

## Structure du dossier booksToScrape (qui contient le code de scrapy)

```bash
│
└── booksToScrape/
       ├── item/                       # Définit la structure des données extraites
       │    ├── genre_item.py          # Item représentant un genre
       │    └── oeuvre_item.py         # Item représentant une œuvre
       │
       ├── loader/                     # Classes pour nettoyer et transformer les données
       │    ├── genre_loader.py        # Prépare et normalise les données des genres
       │    └── oeuvre_loader.py       # Prépare et normalise les données des œuvres
       │
       ├── model/                      # Modèles liés à la persistance (DB)
       │    ├── exchange_rates.py
       │    ├── genre.py
       │    ├── oeuvre_scraping.py
       │    ├── oeuvre.py
       │    └── scraping_logs.py
       │
       ├── pipeline/                   # Traite les items extraits (sauvegarde, validation)
       │    ├── genre_pipeline.py      # Gère le stockage des genres
       │    └── oeuvre_pipeline.py     # Gère le stockage des œuvres
       │
       ├── spiders/                    # Contient les spiders (logique de scraping)
       │    ├── genre_spider.py        # Spider qui extrait les genres
       │    └── oeuvre_spider.py       # Spider qui extrait les œuvres
       │
       ├── middlewares.py              # Middlewares Scrapy (user-agent, proxy, etc.)
       └── settings.py                 # Paramètres Scrapy (pipelines, délais, logs, etc.)
```

## Commande pour Scrapy

1) *pour lancer les spiders (dans l'ordre)*

```bash
# se rendre dans le dossier Scrapy
cd booksToScrape

# lancer le 1er spider
scrapy crawl genre

# lancer le 2e spider
scrapy crawl oeuvre
```
