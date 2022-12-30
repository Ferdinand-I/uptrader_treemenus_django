from django import template
from django.template.defaultfilters import slugify

from ..models import Menu

register = template.Library()


@register.inclusion_tag('includes/menu.html', takes_context=True)
def draw_menu(context, title):
    if ('opened_menu' and 'menu_title' in context and
            context.get('menu_title') == slugify(title)):
        return context
    menu = Menu.objects.filter(
        title__exact=title, items__nesting_level__exact=0).values(
        'items__title', 'items__url'
    )
    if menu:
        return {
            'menu': menu,
            'menu_title': slugify(title)
        }
    return None
