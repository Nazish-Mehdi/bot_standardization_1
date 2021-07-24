import scrapy
from .. items import BotStandItem


class ExampleSpider(scrapy.Spider):
    name = 'example'
    start_urls = ['https://www.amazon.in/s?i=electronics&srs=26297682031&bbn=26297682031&dc&qid=1626265674&ref=lp_specialty-aps_nr_i_0']
    #
    def parse(self, response):
         name = response.xpath('//*[@id="search"]/div[1]/div/div[1]/div/span[3]/div[2]/div[1]/div/span/div/div/div[2]/div[1]/h2/a/span/text()').get()
         price = response.xpath('//*[@id="search"]/div[1]/div/div[1]/div/span[3]/div[2]/div[1]/div/span/div/div/div[2]/div[3]/div[2]/a/span[1]/span[2]/span[2]/text()').get()
         item = BotStandItem()
    #
         print(name,price)
         item['content'] = name,
         item['website_name'] = price
         yield item
    
