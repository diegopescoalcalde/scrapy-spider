import scrapy
from scrapy.loader import ItemLoader
from ..items import ScrapingamazonItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    page_number = 2
    start_urls = ['https://www.amazon.com/s?k=Office+Chair&lo=grid&crid=1N60K12GUA798&qid=1601040579&sprefix=chair&ref=sr_pg_1']

    def parse(self, response):
        items = response.css('.s-asin .sg-col-inner')

        for item in items:
            loader = ItemLoader(item=ScrapingamazonItem(), selector=item)
            loader.add_css('ProductName', '.a-color-base.a-text-normal::text')
            loader.add_css('ProductLink', '.a-link-normal.a-text-normal::attr(href)')
            loader.add_css('ProductPrice', '.a-price-whole::text')
            loader.add_css('ProductReview', 'div.a-size-small > span::attr(aria-label)')
            
            yield loader.load_item()

        next_page = 'https://www.amazon.com/s?k=Office+Chair&lo=grid&page=' + str(AmazonSpiderSpider.page_number) + '&crid=1N60K12GUA798&qid=1601116518&sprefix=chair&ref=sr_pg_' + str(AmazonSpiderSpider.page_number)
        if AmazonSpiderSpider.page_number <= 10:
            AmazonSpiderSpider.page_number += 1
            yield response.follow(next_page, callback = self.parse)