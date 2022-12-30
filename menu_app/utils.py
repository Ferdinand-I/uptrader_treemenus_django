"""Дополнительные утилиты для комфортной работы."""
from django.template.defaultfilters import slugify

from .models import Menu


def get_list_of_nested_objects(slug, menu_title):
    """С помощью параметров slug и menu_title находим все объекты,
    нужные для отрисовки меню.
    """

    # Список параметров, которые нам понадобятся для логики проверки
    items = Menu.objects.values(
        'title', 'items__childs__url', 'items__parent__slug',
        'items__title', 'items__childs__html_prefix', 'items__slug',
        'items__childs__title', 'items__url'
    )
    # Результирующий лист, куда мы будем складывать объекты для отрисовки
    full_res = list()
    while slug:
        cur_nest = list()
        for i in items:
            if i.get('items__slug') == slug:
                cur_nest.append(i)
        for i in cur_nest:
            if i.get('items__childs__title'):
                # Добавляя в результирующий список, формируем шаблон контекста
                full_res.append(
                    {
                        'prefix': i.get('items__childs__html_prefix'),
                        'url': i.get('items__childs__url'),
                        'items__title': i.get('items__childs__title')
                    }
                )
        if len(cur_nest) > 0:
            slug = cur_nest[0].get('items__parent__slug')
        else:
            slug = None
        # Добавление корневых узлов
        if not slug:
            cur_url = ''
            for i in items:
                if not i.get('items__parent__slug') and slugify(i.get(
                        'title')) == menu_title:
                    url = i.get('items__url')
                    if url != cur_url:
                        cur_url = url
                        full_res.append(
                            {
                                'url': i.get('items__url'),
                                'items__title': i.get('items__title')
                            }
                        )
    return full_res[-1::-1]
