# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Question, Choice

"""
后台管理配置文件
"""


# python manage.py createsuperuser
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('问题内容', {'fields': ['question_text']}),
        ('日期信息', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date_str', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


#admin.site.register(Question)
admin.site.register(Question, QuestionAdmin)
