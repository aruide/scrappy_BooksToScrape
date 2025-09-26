from scrapy import Request, Spider
from booksToScrape.loader.oeuvre_loader import OeuvreLoader

class SpiderOeuvre(Spider):
    name = "oeuvre"
    url = "https://books.toscrape.com/"
    
    custom_settings = {
        "ITEM_PIPELINES": {
            "booksToScrape.pipeline.oeuvre_pipeline.OeuvrePipeline": 300
        }
    }
  
    def start_requests(self):
        yield Request( url = self.url, callback= self.parse_oeuvre)
      
    
    def parse_oeuvre(self, response):
        oeuvre_links = response.css(".image_container a::attr(href)").getall()
        
        for link in oeuvre_links:
            url = response.urljoin(link)
            yield Request(url, callback=self.parse_oeuvre_detail)
            
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse_oeuvre)
    
    def parse_oeuvre_detail(self, response):
        loader = OeuvreLoader(response=response)

        loader.add_css("title", ".product_main h1::text")
        loader.add_css("description", "#product_description ~ p::text")
        loader.add_css("rating", "p.star-rating::attr(class)")
        loader.add_css("upc", "table.table.table-striped tr:nth-child(1) td::text")
        loader.add_css("prix_ht", "table.table.table-striped tr:nth-child(3) td::text")
        loader.add_css("taxe", "table.table.table-striped tr:nth-child(5) td::text")
        loader.add_css("nb_available", ".availability::text", re=r"\d+")
        loader.add_css("nb_review", "table.table.table-striped tr:nth-child(7) td::text")
        loader.add_css("image_url", "div.item.active img::attr(src)")
        loader.add_css("genre", "ul.breadcrumb li:nth-child(3) a::text")

        yield loader.load_item()