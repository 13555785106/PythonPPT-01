# -*- coding: utf-8 -*-
import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoSample.settings")
django.setup()
from django.contrib.auth import authenticate
from django.contrib.auth.models import *

# user = User.objects.create_user(username='u001',password='abc')
# User.objects.filter(username='u001').delete()

user = authenticate(username='xiaozh', password='xjfdlj2010')
for up in user.user_permissions.all():
    print up
if user:
    print user
    print user.has_perm('ch03.blog')
    print user.has_module_perms('app100')
print '-----------------------'
user = User.objects.get(username='xiaojf')
if user.check_password('django1234'):
    print user
    print user.has_perm('ch03.blog')
    print user.has_module_perms('app100')
