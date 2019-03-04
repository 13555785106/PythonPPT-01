#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json

data = [
    {'name': 'Tom', 'sex': '男', 'age': 36},
    {'name': 'John', 'sex': '男', 'age': 48},
    {'name': '琼斯', 'sex': '女', 'age': 24},
]

jo = json.dumps(data, ensure_ascii=False, indent=2)
print type(jo)
print jo
