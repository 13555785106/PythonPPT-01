#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoSample.settings")
django.setup()
from ch03.modelssample.hr import *

"""
1.  filter(**kwargs)    结果集匹配指定的条件
2.  exclude(**kwargs)   结果集不匹配指定的条件
"""
print '2002年入职的雇员：'
qs = Emp.objects.filter(hire_date__year=2002)
for item in qs.values():
    print item

print ''.join(['-' for i in xrange(128)])
print '2002年8月入职的雇员：'
qs = Emp.objects.filter(hire_date__year=2002).filter(hire_date__month=8)
for item in qs.values():
    print item

print ''.join(['-' for i in xrange(128)])
print '2001年至2003年入职、月份不是8、天数不是7的雇员：'
qs = Emp.objects.filter(hire_date__year__gte=2001, hire_date__year__lte=2003).exclude(hire_date__month=8).exclude(
    hire_date__day=7)
for item in qs.values():
    print item

print ''.join(['-' for i in xrange(128)])
print '没有部门的的雇员：'
qs = Emp.objects.filter(dep__isnull=True)
for item in qs.values():
    print item
"""
1.  exact   精确匹配,大小写敏感,如果比较的值是None，将被解释为SQL的NULL。
示例:
    Entry.objects.get(id__exact=14)
    Entry.objects.get(id__exact=None)
等价SQL语句:
    SELECT ... WHERE id = 14;
    SELECT ... WHERE id IS NULL;

2.  iexact  与exact一样，但是大小写不敏感。
示例:
    Blog.objects.get(name__iexact='beatles blog')
    Blog.objects.get(name__iexact=None)
等价SQL语句:
    SELECT ... WHERE name ILIKE 'beatles blog';
    SELECT ... WHERE name IS NULL;
    第一条语句会匹配 'Beatles Blog', 'beatles blog', 'BeAtLes BLoG'等等。

3.  contains    包含给定参数，大小写敏感。
示例:
    Entry.objects.get(headline__contains='Lennon')
等价SQL语句:
    SELECT ... WHERE headline LIKE '%Lennon%';

4.  icontains   同contains，大小写不敏感。
示例:
    Entry.objects.get(headline__icontains='Lennon')
等价SQL语句:
    SELECT ... WHERE headline ILIKE '%Lennon%';

5.  in  值在给定的列表中。

示例:
    Entry.objects.filter(id__in=[1, 3, 4])
等价SQL语句:
    SELECT ... WHERE id IN (1, 3, 4);

你也可以用queryset取代列表
    inner_qs = Blog.objects.filter(name__contains='Cheddar')
    entries = Entry.objects.filter(blog__in=inner_qs)
上面的语句等价于如下SQL语句:
    SELECT ... WHERE blog.id IN (SELECT id FROM ... WHERE NAME LIKE '%Cheddar%')
    
如果你传递的是QuerySet的values()或者values_list(), 你必须抽取其中的一列才行:
    inner_qs = Blog.objects.filter(name__contains='Ch').values('name')
    entries = Entry.objects.filter(blog__name__in=inner_qs)
    
下面的语句不正确，将会抛出异常TypeError:
    inner_qs = Blog.objects.filter(name__contains='Ch').values('name', 'id')
    entries = Entry.objects.filter(blog__name__in=inner_qs)
    
使用内嵌查询要考虑数据库的执行性效率，一些数据库，尤其是MySQL,内嵌查询优化的不太好。
在这种情况下，更有效的方式是使用两次查询，先选出列表值，然后传递给第二个查询，而不是使用一条语句。
如下所示：
    values = Blog.objects.filter(name__contains='Cheddar').values_list('pk', flat=True)
    entries = Entry.objects.filter(blog__in=list(values))

6.  gt  大于。

示例:
    Entry.objects.filter(id__gt=4)
等价SQL语句:
    SELECT ... WHERE id > 4;

7.  gte 大于等于。

8.  lt  小于。

9.  lte 小于等于。

10. startswith  大小写敏感的以给定字符串开始。
示例:
    Entry.objects.filter(headline__startswith='Lennon')
等价SQL语句:
    SELECT ... WHERE headline LIKE 'Lennon%';

11. istartswith 同startswith，大小写不敏感。
示例:
    Entry.objects.filter(headline__istartswith='Lennon')
等价SQL语句:
    SELECT ... WHERE headline ILIKE 'Lennon%';

12. endswith    大小写敏感的以给定字符串结尾。
示例:
    Entry.objects.filter(headline__endswith='Lennon')
等价SQL语句:
    SELECT ... WHERE headline LIKE '%Lennon';

13. iendswith   同endswith，大小写不敏感。
示例:
    Entry.objects.filter(headline__iendswith='Lennon')
等价SQL语句:
    SELECT ... WHERE headline ILIKE '%Lennon'

14. range   值在给定范围，包含给定的值
示例:
    import datetime
    start_date = datetime.date(2005, 1, 1)
    end_date = datetime.date(2005, 3, 31)
    Entry.objects.filter(pub_date__range=(start_date, end_date))
等价SQL语句:
    SELECT ... WHERE pub_date BETWEEN '2005-01-01' and '2005-03-31';
注意，如果是DateTime类型，则不包含最后一天，因为日期被转换成如下形式：
    SELECT ... WHERE pub_date BETWEEN '2005-01-01 00:00:00' and '2005-03-31 00:00:00';
你不要混淆 date 和 datetime.

14. date    对于datetime字段，仅比较日期部分。
示例:
    Entry.objects.filter(pub_date__date=datetime.date(2005, 1, 1))
    Entry.objects.filter(pub_date__date__gt=datetime.date(2005, 1, 1))


15. year    对于datetime字段，仅比较年。
示例:
    Entry.objects.filter(pub_date__year=2005)
    Entry.objects.filter(pub_date__year__gte=2005)
等价SQL语句:
    SELECT ... WHERE pub_date BETWEEN '2005-01-01' AND '2005-12-31';
    SELECT ... WHERE pub_date >= '2005-01-01';

16. month   对于datetime字段，仅比较月。
示例:
    Entry.objects.filter(pub_date__month=12)
    Entry.objects.filter(pub_date__month__gte=6)
等价SQL语句:
    SELECT ... WHERE EXTRACT('month' FROM pub_date) = '12';
    SELECT ... WHERE EXTRACT('month' FROM pub_date) >= '6';

17. day 对于datetime字段，仅比较天。
示例:
    Entry.objects.filter(pub_date__day=3)
    Entry.objects.filter(pub_date__day__gte=3)
等价SQL语句:
    SELECT ... WHERE EXTRACT('day' FROM pub_date) = '3';
    SELECT ... WHERE EXTRACT('day' FROM pub_date) >= '3';

18. week    对于datetime字段，仅比较周。Django 1.11中新增。
示例:
    Entry.objects.filter(pub_date__week=52)
    Entry.objects.filter(pub_date__week__gte=32, pub_date__week__lte=38)

19. week_day    对于datetime字段，仅比较周几。周日至周六，数字为1到7。
示例:
    Entry.objects.filter(pub_date__week_day=2)
    Entry.objects.filter(pub_date__week_day__gte=2)


20. time    对于datetime字段，仅比较时间。Django 1.11中新增。
示例:
    Entry.objects.filter(pub_date__time=datetime.time(14, 30))
    Entry.objects.filter(pub_date__time__range=(datetime.time(8), datetime.time(17)))


21. hour    对于datetime或者time字段，仅比较小时。
示例:
    Event.objects.filter(timestamp__hour=23)
    Event.objects.filter(time__hour=5)
    Event.objects.filter(timestamp__hour__gte=12)
等价SQL语句:
    SELECT ... WHERE EXTRACT('hour' FROM timestamp) = '23';
    SELECT ... WHERE EXTRACT('hour' FROM time) = '5';
    SELECT ... WHERE EXTRACT('hour' FROM timestamp) >= '12';

22. minute  对于datetime或者time字段，仅比较分钟。
示例:
    Event.objects.filter(timestamp__minute=29)
    Event.objects.filter(time__minute=46)
    Event.objects.filter(timestamp__minute__gte=29)
等价SQL语句:
    SELECT ... WHERE EXTRACT('minute' FROM timestamp) = '29';
    SELECT ... WHERE EXTRACT('minute' FROM time) = '46';
    SELECT ... WHERE EXTRACT('minute' FROM timestamp) >= '29';

23. second  对于datetime或者time字段，仅比较秒。
示例:
    Event.objects.filter(timestamp__second=31)
    Event.objects.filter(time__second=2)
    Event.objects.filter(timestamp__second__gte=31)
等价SQL语句:
    SELECT ... WHERE EXTRACT('second' FROM timestamp) = '31';
    SELECT ... WHERE EXTRACT('second' FROM time) = '2';
    SELECT ... WHERE EXTRACT('second' FROM timestamp) >= '31';

24. isnull  用来分别表达SQL查询中的 IS NULL 和 IS NOT NULL。
示例:
    Entry.objects.filter(pub_date__isnull=True)
等价SQL语句:
    SELECT ... WHERE pub_date IS NULL;
    
25. regex   大小写敏感的正则匹配
示例:
    Entry.objects.get(title__regex=r'^(An?|The) +')
等价SQL语句:
    SELECT ... WHERE title REGEXP BINARY '^(An?|The) +'; -- MySQL
    SELECT ... WHERE REGEXP_LIKE(title, '^(An?|The) +', 'c'); -- Oracle
    SELECT ... WHERE title ~ '^(An?|The) +'; -- PostgreSQL
    SELECT ... WHERE title REGEXP '^(An?|The) +'; -- SQLite

26. iregex  同regex，大小写不敏感
示例:
    Entry.objects.get(title__iregex=r'^(an?|the) +')
等价SQL语句:
    SELECT ... WHERE title REGEXP '^(an?|the) +'; -- MySQL
    SELECT ... WHERE REGEXP_LIKE(title, '^(an?|the) +', 'i'); -- Oracle
    SELECT ... WHERE title ~* '^(an?|the) +'; -- PostgreSQL
    SELECT ... WHERE title REGEXP '(?i)^(an?|the) +'; -- SQLite
"""
