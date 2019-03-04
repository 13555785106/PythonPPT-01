#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import os
import random
from datetime import datetime, timedelta

# api文档 https://docs.djangoproject.com/en/1.7/ref/models/querysets/
import django

# from django.db.models import Sum,Avg,Count,Q

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chapter19.settings")
django.setup()

from sample.models import Author, Tag, Article, Hobby

Hobby.objects.all().delete()

Hobby(name='篮球').save()
Hobby(name='足球').save()
Hobby(name='排球').save()
# 清除已有Tag对象，新创建以下Tag对象
Tag.objects.all().delete()
for tagName in (u'武侠', u'推理', u'历史', u'言情', u'穿越', u'科幻', u'奇幻', u'玄幻', u'探险', u'恐怖', u'香艳', u'讽刺', u'神魔'):
    # 创建模型对象的第一种方法
    Tag.objects.create(name=tagName)

# 清除已有Author对象，新创建以下Author对象
Author.objects.all().delete()
for i in xrange(10):
    name = ('Smith' if i % 2 == 0 else 'Jones') + ('%02d' % i)
    # 创建模型对象的第二种方法
    author = Author(account=name.lower(), name=name, sex='男' if i % 2 == 0 else '女',
                    birthday=datetime.now() + timedelta(-i),
                    email=(name + '@telecom.com').upper(),
                    mobile='131%08d' % i)

    author.save()

# 清除已有Article对象，新创建以下Article对象
Article.objects.all().delete()
authors = Author.objects.all()
tags = Tag.objects.all()
titles = ['Apple', 'apple', 'APPLE', 'b123ee', 'kill345',
          '老人与海', '红与黑', '双城记', '雾都孤儿', '忏悔录',
          '巴黎圣母院', '红楼梦', '西游记', '荒凉山庄', '悲惨世界',
          '飘', '失乐园', '日瓦戈医生', '麦田里的守望者', '伊利亚特',
          '唐吉坷德', '百年孤独', '变形记', '基督山伯爵', '简爱']
for i in xrange(len(titles)):
    author = random.choice(authors)
    # 创建模型对象的第三种方法
    article = Article()
    article.title = titles[i]
    article.content = 'content%02d' % i
    article.score = i
    article.author = author
    article.release_time = datetime.now() - timedelta(days=random.randint(1, 365), hours=random.randint(1, 24),
                                                      minutes=random.randint(1, 59))
    article.save()
    s = set()
    for m in xrange(3):
        s.add(random.choice(tags))
    for n in s:
        article.tags.add(n)
    article.save()
# 查看模型框架生成的SQL
# print Article.objects.all().query
# 获取所有文章
# print Article.objects.all()

# 结果必须是一条，否则出错
# print Article.objects.get(title='红楼梦')

# 查找title是Apple的文章,区分大小写
# print Article.objects.filter(title='Apple')

# 查找title是Apple的文章,不区分大小写
# print Article.objects.filter(title__iexact='Apple')
# print Article.objects.filter(Q(title__iexact='Apple') & Q(score__gte=1))
# 查找title包含红的文章,区分大小写
# print Article.objects.filter(title__contains='红')

# 查找title包含pp的文章,不区分大小写
# print Article.objects.filter(title__icontains='pp')

# 查找title包含至少一位连续数字的文章
# print Article.objects.filter(title__regex=r"\d+")

# 查找title以字符a开头文章，不区分大小写
# print Article.objects.filter(title__iregex=r"^a.*")

# 查找title以字符a开头文章，不区分大小写，并排除以大写字符A开头的文章
# print Article.objects.filter(title__iregex=r"^a.*").exclude(title__regex=r"^a.*")

# 查找2018年发布的文章
# print Article.objects.filter(release_time__year=2018)

# 删除title以字符a开头文章，不区分大小写
# print Article.objects.filter(title__iregex=r"^a.*").delete()

# 更新title以字符a开头文章，不区分大小写,把title设置成'AAAA'
# Article.objects.filter(title__iregex=r"^a.*").update(title='AAAA')

# 排序
# print Article.objects.all().order_by('score')
# print Article.objects.all().order_by('-score')

# 通过values_list形成元组
# print Author.objects.values_list('name', 'mobile')
# print Author.objects.filter(name__regex=r'^Smith.*').values_list('name', 'mobile')
# print Author.objects.filter(name__regex=r'^Smith.*').values_list('name', flat=True)
# print list(Author.objects.filter(name__regex=r'^Smith.*').values_list('name', flat=True))

# 通过values 获取字典形式的结果
# print Author.objects.values('name', 'mobile')
# print list(Author.objects.values('name', 'mobile'))
# print [item for item in Author.objects.filter(name__contains='Smith').values('name', 'mobile')]

# extra 实现 别名，条件，排序等
# print Author.objects.filter(name__contains='Smith').extra(
#    select={'author_name': 'name', 'author_mobile': 'mobile'}).query
# print Author.objects.filter(name__contains='Smith').extra(
#    select={'author_name': 'name', 'author_mobile': 'mobile'}).defer('name').query
# print Article.objects.all().extra(select={'is_pass': "score > 10"}).query
# for article in Article.objects.all().extra(select={'is_pass': "score > 10"}):
#    print article.is_pass

# for article in Article.objects.all().extra(where=["score > 15 AND score <20"],order_by=['-score']):
#    print article.score

# annotate 计数，求和，平均数

# print Article.objects.all().values('author_id').annotate(count=Count('author_id')).values('author_id', 'count')
# print Article.objects.all().values('author_id').annotate(score_sum=Sum('score')).values('author_id', 'score_sum')
# print Article.objects.all().values('author_id').annotate(score_avg=Avg('score')).values('author_id', 'score_avg')

# defer 排除不需要的字段
# print Author.objects.all().query
# print Author.objects.all().defer('name','sex','mobile').query
# 排除后，就不应再去获取，会导致二次查询！反而降低了效率
# for v in Author.objects.all().defer('name','sex','mobile'):
#     print v.name

# only 仅选择需要的字段
# print Author.objects.all().only('name','sex','mobile').query
# for v in Author.objects.all().only('name','sex','mobile'):
#    print v.birthday

# print Article.objects.dates('release_time', 'year')
# print Article.objects.first()
# print Article.objects.last()

# print Article.objects.latest('release_time')
# print Article.objects.earliest('release_time')

# tag0 = Tag.objects.all()[0]
# print tag0
# for a in tag0.article_set.all():
#    print a
