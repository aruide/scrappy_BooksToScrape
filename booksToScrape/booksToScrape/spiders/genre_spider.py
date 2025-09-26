from scrapy import Request, Spider
from ..items import GenreItem


class SpiderGenre(Spider):
    name = "genre"
    url = "https://books.toscrape.com/"
    
    def start_requests(self):
        yield Request( url = self.url, callback= self.parse_genre)
        
    
    def parse_genre(self, response):
        listegenre = response.css('ul.nav-list li ul li')
        
        for genre in listegenre:
                name = genre.css('a::text').extract_first()
                
                item = GenreItem()
                
                item["name"] = name
                
                yield item 