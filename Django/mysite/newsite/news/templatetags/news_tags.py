from django import template
from news.models import *
from django.db.models import Count

register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.annotate(cnt=Count('news')).filter(cnt__gt=0)