from datetime import datetime

import scrapy
from scrapy import Selector
from scrapy.loader import ItemLoader
from scrapy.loader.processors import *

html = u"""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>雇员列表</title>
</head>
<body>
<table>
    <caption>雇员列表</caption>
    <tr>
        <th>姓名</th>
        <th>性别</th>
        <th>生日</th>
        <th>月薪</th>
        <th>爱好</th>
    </tr>
    <tr>
        <td>Tom</td>
        <td>male</td>
        <td>1999-03-09</td>
        <td>7889</td>
        <td>
            <ul>
                <li>篮球</li>
                <li>足球</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td>Jones</td>
        <td>female</td>
        <td>2000-06-10</td>
        <td>8000</td>
        <td>
            <ul>
                <li>排球</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td>John</td>
        <td>male</td>
        <td>1998-02-27</td>
        <td>10000</td>
        <td>
        </td>
    </tr>
</table>
</body>
</html>
"""


def to_date(str_date):
    print(str_date)
    return datetime.strptime(str_date, '%Y-%m-%d').date()


class EmpItem(scrapy.Item):
    name = scrapy.Field(output_processor=TakeFirst(), )
    sex = scrapy.Field(input_processor=MapCompose(lambda v: '男' if v == 'male' else '女'),
                       output_processor=TakeFirst(), )
    birthday = scrapy.Field(input_processor=MapCompose(to_date, ), output_processor=TakeFirst(), )
    salary = scrapy.Field(output_processor=Compose(TakeFirst(), int), )
    hobbies = scrapy.Field(output_processor=Join(','), )


selector = Selector(text=html, type="html")
for s in selector.xpath("//tr[position()>1]"):
    itemloader = ItemLoader(item=EmpItem(), selector=s)
    itemloader.add_xpath('name', "./td[position()=1]/text()")
    itemloader.add_xpath('sex', "./td[position()=2]/text()")
    itemloader.add_xpath('birthday', "./td[position()=3]/text()")
    itemloader.add_xpath('salary', "./td[position()=4]/text()")
    itemloader.add_xpath('hobbies', "./td[position()=5]/ul/li/text()")
    print(itemloader.load_item())
