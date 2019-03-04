#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoSample.settings")
django.setup()
from ch03.models import *

# 清除所有Author数据
Author.objects.all().delete()

# 通过管理器的create方法创建对象
author_abel = Author.objects.create(name='Abel', email='abel@163.com')
author_abraham = Author.objects.create(name='Abraham', email='abraham@sohu.com')
author_alan = Author.objects.create(name='Alan', email='alan@163.com')
author_alva = Author.objects.create(name='Alva', email='alva@sohu.com')
author_alex = Author.objects.create(name='Alex', email='alex@163.com')
author_andy = Author.objects.create(name='Andy', email='andy@sohu.com')
author_arthur = Author.objects.create(name='Arthur', email='arthur@163.com')
author_terry = Author.objects.create(name='Terry', email='terry@sohu.com')
author_tom = Author.objects.create(name='Tom', email='tom@163.com')
author_tony = Author.objects.create(name='Tony', email='tony@sohu.com')

# 清除所有Blog数据
Blog.objects.all().delete()

# 通过构造函数创建对象
blog_servlet = Blog(name='Servlet Tutorial', keywords='java,servlet,jsp,web', content="""Servlet technology ...""")
# 必须调用save进行保存
blog_servlet.save()

blog_django = Blog(name='Django Tutorial', keywords='python,django,web')
blog_django.content = """Because Django was ."""
blog_django.save()
blog_android = Blog(name='Android Development', keywords='java,android,mobile')
blog_android.content = """Explore the Android phones, tablets, wearables, ..."""
blog_android.save()
# 清除所有Entry数据
Entry.objects.all().delete()

# 一对多关系可以在创建对象时直接建立
entry_servlet01 = Entry.objects.create(blog=blog_servlet, headline='An apple', body_text='', pub_date='2017-3-6',
                                       click_count=50)
# 多对多关系必须在对象创建之后建立 ！！！！！
entry_servlet01.authors = [author_abel, author_abraham]

entry_servlet02 = Entry.objects.create(blog=blog_servlet, headline='Apple is red', body_text='', pub_date='2017-3-6',
                                       click_count=75)
entry_servlet02.authors.add(author_abel, author_alan, author_terry, author_tom)

entry_servlet03 = Entry.objects.create(blog=blog_servlet, headline='Apple is green', body_text='',
                                       pub_date='2017-5-1',
                                       click_count=100)
entry_servlet03.authors = [author_abel, author_abraham, author_terry, author_tom, author_tony]

entry_django01 = Entry.objects.create(blog=blog_django, headline='Apple is red', body_text='', pub_date='2017-5-1',
                                      click_count=25)
entry_django01.authors = [author_alex, author_andy, author_arthur, author_tom]

entry_django02 = Entry.objects.create(blog=blog_django, headline='Apple is green', body_text='', pub_date='2017-5-1',
                                      click_count=50)
entry_django02.authors = [author_alan, author_alva, author_arthur]

entry_django03 = Entry.objects.create(blog=blog_django, headline='An apple', body_text='', pub_date='2018-6-5',
                                      click_count=75)
entry_django03.authors = [author_tom]

entry_android01 = Entry.objects.create(blog=blog_android, headline='Apple is red', body_text='',
                                       pub_date='2017-6-22',
                                       click_count=5)
entry_android01.authors = [author_arthur, author_terry]

entry_android02 = Entry.objects.create(blog=blog_android, headline="Peach is good", body_text='',
                                       pub_date='2020-9-1',
                                       click_count=125)
entry_android02.authors = [author_terry, author_tom]
