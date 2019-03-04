# -*- coding: utf-8 -*-

import scrapy.http

from Spider.items import ImageItem

"""
scrapy crawl iconarchive01 -o iconarchive01.json -s LOG_FILE=iconarchive01.log 
"""


class Iconarchive01Spider(scrapy.Spider):
    name = 'iconarchive01'
    allowed_domains = ['iconarchive.com']
    start_urls = ['http://www.iconarchive.com/']
    custom_settings = {
        'FILES_STORE': 'images01',
        'FILES_URLS_FIELD': 'image_urls',
        'FILES_RESULT_FIELD': 'image_path',
        'ITEM_PIPELINES': {
            'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
            'Spider.middlewares.UserAgentMiddleware': 500,
            'scrapy.pipelines.files.FilesPipeline': 300,
        }
    }

    def parse(self, response):
        image_urls = response.xpath("//img[contains(@src,'/512/')]/@src").extract()
        if image_urls:
            si = ImageItem()
            si['image_urls'] = response.xpath("//img[contains(@src,'/512/')]/@src").extract()
            yield si
        for href in response.xpath("//a/@href").re(r".*\.html"):
            yield response.follow(href, callback=self.parse)


"""
parse(self,response):当请求url返回网页没有指定回调函数，默认的Request对象的回调函数，
用来处理网页返回的response，和生成的Item或者Request对象

parse（）方法的工作机制：

1.因为使用的yield，而不是return，parse函数将会当做一个生成器使用，
scrapy会注意调用parse方法中生成的结果，并且判断该结果是一个什么样的类型。
2.如果是request则会加入爬取队列中，如果是item类型则会使用pipeline处理，
其他类型则会返回错误信息。
3.scrapy取到第一部分的request不会立马就去发送request，
只是将这个request放到队列中，然后接着从生成器中获取。
4.取完了第一部分的request，然后再获取第二部分的item，
取到item了，就会放到对应的pipeline中处理。
5.parse方法作为回调函数（callback），赋值给Request,
指定parse()方法处理这些请求scrapy.Request(url,callback=self.parse)。
6.Request对象经过调度，执行生成scrapy.http.response()响应对象，
并送回parse()方法，直到调度器中没有Requset（递归的思路）。
7.取尽之后，parse()工作结束，引擎再根据对列和pipeline中的内容去执行相应的操作。
8.程序在取得各个页面的items前，会先处理完之前所有的request对列的请求，然后再提取items。
"""