# Scrapyd & ScrapydWeb

Ce projet ne se limite pas à Scrapy : pour faciliter le déploiement et la gestion des spiders, j'utilise :

- Scrapyd → un service qui permet de lancer et gérer les spiders via une API REST.

- ScrapydWeb → une interface web qui simplifie le suivi, le lancement et la planification des spiders hébergés sur Scrapyd.

## Scrapyd

Scrapyd est un serveur qui permet de déployer et exécuter des spiders Scrapy sans avoir besoin d’ouvrir un terminal à chaque fois.

Il expose une API REST qui permet :

- d’ajouter des projets Scrapy,
- de lancer des spiders,
- de planifier des jobs,
- de récupérer l’état et les logs.

### Commande

1) *lancer le serveur scrapyd*
```bash
scrapyd
```

2) *déployer un projet Scrapy*

> [!WARNING]  
> Pour que la commande fonctionne, il faut que le serveur Scrapyd soit lancé. 


```bash
scrapyd-deploy local -p "nom du projet dans scrapy.cfg donc booksToScrape"

```

### URL

URL de scrapyd: http://127.0.0.1:6800

## ScrapydWeb

ScrapydWeb est une interface graphique web qui permet de :

- Lancer et arrêter les spiders,
- Suivre les jobs en cours, terminés ou échoués,
- Consulter les logs,
- Programmer l’exécution de spiders.

C’est une surcouche visuelle à Scrapyd, beaucoup plus conviviale que l’API seule.

### Commande
> [!WARNING]  
> Ne pas oublier de se mettre dans l'environnement virtuel `.venv_scrapydweb`.  

1) *lancer le serveur scrapydweb*
```bash
scrapydweb
```

### Fonctionnalités principales

- ✅ Lancer un spider en un clic
- ✅ Voir l’historique des exécutions
- ✅ Consulter les logs directement depuis le navigateur
- ✅ Programmer des tâches récurrentes

### URL

URL de scrapydweb: http://127.0.0.1:5000