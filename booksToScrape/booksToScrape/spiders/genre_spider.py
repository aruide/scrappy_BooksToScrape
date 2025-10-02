from scrapy import Request, Spider
from booksToScrape.item.genre_item import GenreItem
from booksToScrape.loader.genre_loader import GenreLoader

class SpiderGenre(Spider):
    name = "genre"
    url = "https://books.toscrape.com/"
    
    custom_settings = {
        "ITEM_PIPELINES": {
            "booksToScrape.pipeline.genre_pipeline.GenrePipeline": 200
        }
    }
    
    def start_requests(self):
        yield Request( url = self.url, callback= self.parse_genre)
        
    
    def parse_genre(self, response):
        
        listegenre = response.css('ul.nav-list li ul li')
        
        for genre in listegenre:
                
                loader = GenreLoader(item = GenreItem(), selector=genre)
                loader.add_css('name', 'a::text')
                yield loader.load_item()