import datetime
from django import template

register = template.Library()
@register.simple_tag()
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)

@register.simple_tag()
def untitled():
    pass