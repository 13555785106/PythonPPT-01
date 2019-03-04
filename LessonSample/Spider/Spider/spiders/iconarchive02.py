# -*- coding: utf-8 -*-

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from Spider.items import ImageItem

"""
scrapy crawl iconarchive02 -o iconarchive02.json -s LOG_FILE=iconarchive02.log 
"""


class Iconarchive02Spider(CrawlSpider):
    name = 'iconarchive02'
    allowed_domains = ['iconarchive.com']
    start_urls = ['http://iconarchive.com/']
    custom_settings = {
        'IMAGES_STORE': 'images02',
        'IMAGE_URLS_FIELD': 'image_urls',
        'IMAGES_RESULT_FIELD': 'image_path',
        'ITEM_PIPELINES': {
            'scrapy.pipelines.images.ImagesPipeline': 300,
            'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
            'Spider.middlewares.UserAgentMiddleware': 500,
        }
    }
    rules = (
        Rule(LinkExtractor(allow=(r"^http://.*?\.html$")), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        image_urls = response.xpath("//img[contains(@src,'/512/')]/@src").extract()
        if image_urls:
            si = ImageItem()
            si['image_urls'] = response.xpath("//img[contains(@src,'/512/')]/@src").extract()
            yield si


"""

LinkExtractor构造器参数：
allow   接收一个正则表达式或一个正则表达式列表，提取绝对url与正则表达式匹配的链接。
        如果该参数为空（默认），就提取全部链接。
deny    接收一个正在则表达式或一个正则表达式列表，与allow相反，排除绝对url与正则表达式匹配的链接。
allow_domains   接收一个域名或一个域名列表，提取到指定域的链接
deny_domains    与allow_domains相反，排除指定域的链接
restrict_paths  接收一个XPath表达式或一个XPath表达式列表，提取XPath表达式选中区域下的链接
restrict_css    接收一个CSS选择器或一个CSS选择器列表，提取CSS选择器选中区域下的链接
tags    接收一个标签/标签列表，提取指定标签内的链接，默认为 ['a','area']
attrs   接收一个属性/属性列表，提取指定属性内的链接，默认为 ['href']
process_value   接收一个形如func(value)的回调函数，如果传递了该参数，
                LinkExtractor将调用该回调函数对提取的每一个链接进行处理，
                回调函数正常情况下应返回一个字符串，想要抛弃所处理的链接时，返回None
"""
