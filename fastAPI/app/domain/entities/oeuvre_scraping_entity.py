from dataclasses import dataclass

@dataclass
class OeuvreScrapingEntity:
    """
    Entité représentant la relation entre une œuvre et un log de scraping.

    Attributes:
        oeuvre_fk (int): Clé étrangère vers l'œuvre.
        scraping_log_fk (int): Clé étrangère vers le log de scraping.
    """
    oeuvre_fk: int
    scraping_log_fk: int
