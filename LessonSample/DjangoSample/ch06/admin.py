# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.core import serializers
from django.http import HttpResponse

from models import *


class UserExtraAdmin(admin.ModelAdmin):
    verbose_name = "用户附加信息"
    verbose_name_plural = verbose_name
    empty_value_display = '-空-'
    labels = {'sex': '性别'}
    fields = ('user', ('sex', 'birthday'), ('email', 'mobile'))
    list_display = ('user', 'sex', 'birthday', 'email', 'mobile')
    list_editable = ('birthday',)
    list_filter = ('user__username', 'sex', 'birthday')
    list_per_page = 10
    radio_fields = {"sex": admin.HORIZONTAL}
    search_fields = ['user__username']
    show_full_result_count = True
    view_on_site = True
    ordering = ['user__username']
    actions = ['make_male', 'make_female', 'export_as_json']

    def make_male(self, request, queryset):
        queryset.update(sex='男')

    make_male.short_description = "设置为男性"

    def make_female(self, request, queryset):
        queryset.update(sex='女')

    make_female.short_description = "设置为女性"

    def export_as_json(self, request, queryset):
        response = HttpResponse(content_type="application/json")
        serializers.serialize("json", queryset, stream=response)
        return response

    export_as_json.short_description = "导出为JSON"


admin.site.register(UserExtra, UserExtraAdmin)
