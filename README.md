# uptrader_treemenus_django
Тестовое задание для компании **UpReader**. Веб приложение с утилитами для отрисовки древовидных меню.

<img src="https://www.alwaysdata.com/static/img/landings/django-logo.png" width=180> <img src="https://cdn-user84060.skyeng.ru/uploads/5fdb29ffa122b628754296.png" width=128> 

Данный сервис написано с помощью фреймворка **Django** и предоставляет возможности для отрисовки древовидных меню. Меню реализованы с помощью **Django templates** и кастомных **teplate tags.**

### Чтобы запустить:

Клонируйте репозиторий в директорию, из которой будете запускать проект:

```BASH
git@github.com:Ferdinand-I/uptrader_treemenus_django.git
```

Перейдите в директорию проекта:

```BASH
cd uptrader_treemenus_django/
```

Создайте виртуальное окружение и активируйте его:

```BASH
python -m venv venv
source venv/Scripts/activate/
```

Установите зависимости:

```BASH
pip install -r requirements.txt
```

Сделайте миграции:

```BASH
python manage.py migrate
```

Создайте суперпользователя:

```BASH
python manage.py createsuperuser
```

Чтобы запустить локальный сервер для тестов:

```BASH
python manage.py runserver
```

Ура! Сервис запущен локально и готов к работе!

Чтобы создать меню, зарегистрируйтес в админке http://127.0.0.1:8000/admin/

Админ-интерфейс для создания меню: http://127.0.0.1:8000/admin/menu_app/category/add/

Чтобы отрисовать меню на главной странице *index.html*, которая находится в **./templates/main/**, создайте тэг вида *{% draw_menu 'Название меню' %}*

P.S.
Важно!!!
В будущих обновлениях будут фиксы сортировки пунктов меню.

