# -*- coding: utf-8 -*-

from django import template

register = template.Library()


def underscore_var_value(value, arg):
    """获取字典中以下划线开头的变量"""
    return value[arg]


register.filter('uvv', underscore_var_value)
