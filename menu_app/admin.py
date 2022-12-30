from django.contrib import admin
from .models import Category, Menu


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    pass
