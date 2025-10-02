# Installation

> [!WARNING]  
> Ce projet utilise **deux environnements virtuels distincts** afin d’éviter les conflits de dépendances.  
> 
> - L’environnement `venv_scrapy` qui contient Scrapy, FastAPI, Scrapyd.  
> - L’environnement `venv_scrapydweb` qui contient ScrapydWeb.  
> 
> Cette séparation est nécessaire car certaines dépendances (ex : `SQLAlchemy`, `Flask-SQLAlchemy`, `apscheduler`) exigent des versions incompatibles entre elles.  


1) clonage du projet GitHub
```bash
git clone https://github.com/aruide/scrappy_BooksToScrape.git
```

2) création du `.venv` (pour scrapy, scrapyd + fastAPI)
```bash
# création du .venv
python -m venv .venv

# activer l'environnement virtuel
source .venv/Scripts/activate

# installer les dependances
pip install -r requirements.txt
```

3) création de `.venv_scrapydweb` (pour scrapydweb)
```bash
# création du .venv_scrapydweb
python -m venv .venv_scrapydweb

# activer l'environnement virtuel
source .venv_scrapydweb/Scripts/activate

# installer les dependances
pip install -r requirements_scrapydweb.txt
```

## pour l'environnement `.venv`

1) lancer une commande scrapy + lancer le serveur scrapyd
```bash
# allez dans le chemin de scrapy
cd booksToScrape

# lancer une pipeline
scrapy crawl [nom de la pipeline] # genre ou oeuvre

# lancer scrapyd
scrapyd
```

2) lancer fastAPI
```bash
# allez dans le chemin de scrapy
cd fastAPI

# lancer le serveur
uvicorn app.main:app --reload
```

## pour l'environnement `.venv_scrapydweb`

1) lancer scrapydweb
```bash
# allez dans le chemin de scrapy
cd booksToScrape

# lancer scrapydweb
scrapydweb
```