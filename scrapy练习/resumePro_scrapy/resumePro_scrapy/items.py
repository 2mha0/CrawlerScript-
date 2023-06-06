# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ResumeproScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    download_href = scrapy.Field()
    detail_href = scrapy.Field()

