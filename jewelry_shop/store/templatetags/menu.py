from django import template

register = template.Library()

from store.models import Category


@register.inclusion_tag('core/menu.html')

def menu():
    categories = Category.objects.all()
    return {'categories':categories}