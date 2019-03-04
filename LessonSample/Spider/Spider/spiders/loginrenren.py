# -*- coding: utf-8 -*-

import scrapy
from scrapy.http import Request, FormRequest

"""
scrapy crawl loginsinablog
"""


class LoginRenRenSpider(scrapy.Spider):
    name = 'loginrenren'
    allowed_domains = ['renren.com']

    def start_requests(self):
        return [Request('http://www.renren.com/', callback=self.login, )]

    def login(self, response):
        fo = open("loginrenren01.html", "wb")
        fo.write(response.body)
        fo.close()
        return FormRequest.from_response(response, formdata={'email': '13555785106', 'password': 'xjfdlj2010'},
                                         callback=self.parse, )

    def parse(self, response):
        fo = open("loginrenren02.html", "wb")
        fo.write(response.body)
        fo.close()
