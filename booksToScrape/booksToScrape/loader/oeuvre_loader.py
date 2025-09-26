import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose, TakeFirst
from booksToScrape.item.oeuvre_item import OeuvreItem

def strip_text(value):
    return value.strip() if value else value

def parse_price(value):
    """Transforme '£53.74' → 53.74"""
    return float(value.replace("£", "").strip())

def parse_int(value):
    """Transforme '22' (ou '22 available') → 22"""
    try:
        return int(value)
    except:
        return None

def parse_rating(value):
    """Transforme 'star-rating Three' → 3"""
    rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    for k, v in rating_map.items():
        if k in value:
            return v
    return 0

class OeuvreLoader(ItemLoader):
    default_item_class = OeuvreItem
    default_output_processor = TakeFirst()
    default_input_processor = MapCompose(strip_text)

    prix_ht_in = MapCompose(strip_text, parse_price)
    taxe_in = MapCompose(strip_text, parse_price)
    nb_available_in = MapCompose(strip_text, parse_int)
    nb_review_in = MapCompose(strip_text, parse_int)
    rating_in = MapCompose(strip_text, parse_rating)
