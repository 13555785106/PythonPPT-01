#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json

dictStr = {"city": "北京", "name": "大刘"}
json.dump(dictStr, open("dictStr.json", "w"), ensure_ascii=False)
