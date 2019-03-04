# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse


def my404(request):
    response = HttpResponse("哈哈哈，找不到")
    response.status_code = 404
    return response
