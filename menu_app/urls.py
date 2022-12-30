from django.urls import path
from .views import menu_view


urlpatterns = [
    path('', menu_view, name='menu_view'),
    path('<slug:menu_title>/<slug:slug>/', menu_view, name='items_view'),
]
