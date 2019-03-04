#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json

data = '''
[
  {
    "age": 80, 
    "name": "Tom", 
    "sex": "男"
  }, 
  {
    "age": 80, 
    "name": "John", 
    "sex": "男"
  }, 
  {
    "age": 24, 
    "name": "琼斯", 
    "sex": "女"
  }
]
'''

jo = json.loads(data)
print type(jo)
for emp in jo:
    for k, v in emp.items():
        print k, '=', v
