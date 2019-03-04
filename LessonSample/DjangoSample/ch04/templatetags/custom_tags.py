# -*- coding: utf-8 -*-
import datetime

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')


register.filter('cut', cut)


@register.filter
@stringfilter
def lower(value):
    return value.lower()


@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)


@register.simple_tag(name='minustwo')
def minus_two(value):
    return value - 2


@register.inclusion_tag('ch03/show_ul.html')
def show_ul(val):
    return {'lis': val}


@register.tag(name="upper")
def do_upper(parser, token):
    nodelist = parser.parse(('endupper',))
    parser.delete_first_token()
    return UpperNode(nodelist)

class UpperNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist
    def render(self, context):
        output = self.nodelist.render(context)
        return output.upper()
