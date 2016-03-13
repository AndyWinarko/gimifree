from scrapy import Spider
from scrapy.selector import Selector
from gimifree.items import GimifreeItem

class PackpubSpider(Spider):
    name = "packpub"
    allowed_domains = ["packtpub.com"]
    start_urls = [
        "https://www.packtpub.com/packt/offers/free-learning"
    ]

    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="dotd-main-book-summary float-left"]')

        for question in questions:
            item = GimifreeItem()
            item['title'] = question.xpath('div[@class="dotd-title"]/h2').extract()[0]
            yield item
