# -*- coding: utf-8 -*-

import scrapy
from scrapy.http import Request

"""
scrapy crawl loginsinablog
"""


class LoginSinaBlogSpider(scrapy.Spider):
    name = 'loginsinablog'
    allowed_domains = ['sina.com.cn']

    def start_requests(self):
        cookies = {'SINAGLOBAL': '182.200.31.79_1511336804.608122',
                   'U_TRS1': '00000093.2901701c.5a220ad2.93570d10',
                   'SGUID': '1512203153480_97683729',
                   'vjuids': '-5c85112d7.1654d6b0325.0.323a9a04cf626',
                   'vjlast': '1539139953',
                   'UOR': ',,',
                   'bdshare_firstime': '1550747205338',
                   'lxlrttp': '1549280986',
                   'SCF': 'AhGlL2ri9x5DQK01sYPTKKvE2EX2Nid9CPUXeZWNA0RlzENuGLYZURih7ERpJD4agSJpo7QFG4oO9uRZEfH65RE.',
                   'U_TRS2': '000000d4.f42743e5.5c7a9aeb.fc166387',
                   'WEB2': 'bcc336fc1d15322a8c4a8bfacce34707',
                   'Apache': '182.200.27.212_1551538999.373032',
                   'ULV': '1551539097793:2:2:2:182.200.27.212_1551538999.373032:1551538999780',
                   'ULOGIN_IMG': 'yf-5095f732d49a48288ef3d8f13c2591010425',
                   'SUB': '_2A25xfu8pDeRhGeVI7lYY9CjNzD6IHXVSCkfhrDV_PUNbm9ANLRL8kW9NT-FIej4jCqZLg75FtPDdhQdRQZUyhdks',
                   'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9WhO.fZm4SWJeugbFHrGaIop5NHD95Q0So-X1KBceKMEWs4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNe0qfSh.XSo2Nentt',
                   'ALF': '1583076089',
                   'sso_info': 'v02m6alo5qztKWRk5yljpOQpZCToKWRk5iljoOgpZCjnLONo5S0jpOQtoyTnLKJp5WpmYO0s42jlLSOk5C2jJOcsg=='}

        return [Request('http://my.sina.com.cn/', cookies=cookies, callback=self.parse, )]

    def parse(self, response):
        fo = open("loginsinablog.html", "wb")
        fo.write(response.body)
        fo.close()
        # return Request("http://my.sina.com.cn/", callback=self.parse, )
