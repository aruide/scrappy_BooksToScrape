import scrapy


class OeuvreItem(scrapy.Item):
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