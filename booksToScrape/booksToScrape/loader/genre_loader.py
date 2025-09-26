from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose, TakeFirst


class GenreLoader(ItemLoader):
    # par défaut : prend uniquement la première valeur
    default_output_processor = TakeFirst()

    # nettoyage spécifique pour le champ "name"
    name_in = MapCompose(str.strip)
