#!/usr/bin/python
# -*- coding: UTF-8 -*-

dic = {"name": "xiaojf", "age": 45, "sex": "male"}
dic['address'] = "LiaoNing ShenYang"

print dic
print dic["name"]
print dic.get("phone")
print dic["phone"]  # 无此键，此种方式会出错
