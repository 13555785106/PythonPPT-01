# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import *

from quotesbot.items import QuoteItem


class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'toscrape-itemloader'
    start_urls = [
        'http://quotes.toscrape.com/',
    ]

    def parse(self, response):
        for quote in response.xpath('//div[@class="quote"]'):
            item_loader = ItemLoader(item=QuoteItem(), selector=quote)
            item_loader.add_xpath("text", './span[@class="text"]/text()')
            item_loader.add_xpath("author", './/small[@class="author"]/text()', TakeFirst())
            item_loader.add_xpath("tags", './/div[@class="tags"]/a[@class="tag"]/text()',
                                  MapCompose(str.upper))
            yield item_loader.load_item()

        next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
