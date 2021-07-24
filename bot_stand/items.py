# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BotStandItem(scrapy.Item):
    # define the fields for your item here like:
    content=scrapy.Field()
    website_name=scrapy.Field()