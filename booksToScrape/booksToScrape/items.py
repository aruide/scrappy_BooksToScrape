# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OeuvreItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    description = scrapy.Field()
    rating = scrapy.Field()
    upc = scrapy.Field()
    prix_ht = scrapy.Field()
    taxe = scrapy.Field()
    nb_available = scrapy.Field()
    nb_review = scrapy.Field()
    image_url = scrapy.Field()
    genre = scrapy.Field()
    pass

class GenreItem(scrapy.Item):
    name = scrapy.Field()
    pass