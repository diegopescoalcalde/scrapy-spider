# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapingamazonItem(scrapy.Item):
    # define the fields for your item here like:
    ProductName = scrapy.Field()
    ProductLink = scrapy.Field()
    ProductPrice = scrapy.Field()
    ProductReview = scrapy.Field()
    ImageLink = scrapy.Field()
    pass
