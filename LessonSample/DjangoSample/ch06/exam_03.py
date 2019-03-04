# -*- coding: utf-8 -*-
import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoSample.settings")
django.setup()
from django.contrib.auth.models import *

# contentType = ContentType.objects.create(app_label='app100', model='file')
# p01 = Permission.objects.create(codename='add', name='添加文件', content_type=contentType)
# p02 = Permission.objects.create(codename='chg', name='修改文件', content_type=contentType)
# p03 = Permission.objects.create(codename='del', name='删除文件', content_type=contentType)
contentType = ContentType.objects.get(app_label='app100', model='file')
print contentType.id, contentType.app_label, contentType.model
for permission in contentType.permission_set.all():
    print '    ', permission
