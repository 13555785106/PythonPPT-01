# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ImageItem(scrapy.Item):
    image_urls = scrapy.Field()
    image_path = scrapy.Field()


class EmpItem(scrapy.Item):
    name = scrapy.Field()
    sex = scrapy.Field()
    birthday = scrapy.Field()
    salary = scrapy.Field()
    hobbies = scrapy.Field()
