# from scrapy import Request, Spider
# from ..items import Oeuvre


# class SpiderOeuvre(Spider):
#     name = "oeuvre"
#     url = "https://books.toscrape.com/"
    
#     def start_requests(self):
#         yield Request( url = self.url, callback= self.parse_oeuvre)
        
    
#     def parse_oeuvre(self, response):
#         listeOeuvre = 