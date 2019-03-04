# -*- coding: utf-8 -*-

import scrapy
from scrapy.http import Request, FormRequest

"""
scrapy crawl loginlocalhost
"""


class LoginSinaBlogSpider(scrapy.Spider):
    name = 'loginlocalhost'
    allowed_domains = ['localhost']

    def start_requests(self):
        return [Request('http://localhost:9090/WebSample/Login', callback=self.login, )]

    def login(self, response):
        fo = open("loginlocalhost01.html", "wb")
        fo.write(response.body)
        fo.close()
        for v in response.headers:
            print(v, response.headers[v])
        formdata = {"account": "sa", "passwd": "123456", }
        request = FormRequest.from_response(response, callback=self.parse,
                                            formdata=formdata, )
        print("-" * 64)
        for v in request.headers:
            print(v, request.headers[v])
        return request

    def parse(self, response):
        fo = open("loginlocalhost02.html", "wb")
        fo.write(response.body)
        fo.close()
        return Request('http://localhost:9090/WebSample/sample/ex03/ListUser', )
