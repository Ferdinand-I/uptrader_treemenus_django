from django.shortcuts import render

from .utils import get_list_of_nested_objects


def menu_view(request, **kwargs):
    """Вью-функция, логика которой зависит от переданных в url параметров."""
    if not kwargs:  # Отрисовываем в шаблоне только корневые узлы меню
        return render(
            request, template_name='main/index.html', context={'title': 'Меню'}
        )
    if kwargs:
        # Достаём аргументы из url, формируем с их помощью
        # список нужных объектов
        menu_title, slug = kwargs.get('menu_title'), kwargs.get('slug')
        menu = get_list_of_nested_objects(slug, menu_title)
        return render(
            request,
            template_name='main/index.html',
            context={
                'opened_menu': menu,
                'menu_title': menu_title
            }
        )
