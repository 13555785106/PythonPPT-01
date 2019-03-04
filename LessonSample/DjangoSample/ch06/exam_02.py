# -*- coding: utf-8 -*-
import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoSample.settings")
django.setup()
from django.contrib.auth.models import *

print '---------Users---------'
for user in User.objects.all():
    print user.id, user.username
print '---------Groups---------'
for group in Group.objects.all():
    print group.id, group.name
    for p in group.permissions.all():
        print p, p._meta.verbose_name, p.content_type.name
print '---------ContentTypes---------'
for content_type in ContentType.objects.all():
    print content_type.id, content_type.app_label, content_type.model
print '---------Permissions---------'
for permission in Permission.objects.all():
    print permission.id, permission.content_type.id, permission.codename, permission.name
