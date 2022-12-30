from django.db import models
from django.shortcuts import reverse
from django.template.defaultfilters import slugify
from django.utils.translation import gettext as _


class Category(models.Model):
    """Объект элемента меню."""
    menu = models.ForeignKey(
        'Menu',
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name=_('Menu'),
        blank=True,
        null=True
    )
    title = models.CharField(
        max_length=128,
        verbose_name=_('Name of the menu item')
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='childs',
        verbose_name=_('Parent'),
        blank=True,
        null=True
    )
    slug = models.SlugField(unique=True)
    nesting_level = models.PositiveSmallIntegerField(default=0, editable=False)
    url = models.URLField(default='_', editable=False)
    html_prefix = models.CharField(
        max_length=128,
        default='',
        editable=False
    )

    class Meta:
        ordering = ['title']

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, **kwargs):
        if self.parent:
            # Вычисляем уровень вложенности относительно родителя
            self.nesting_level = self.parent.nesting_level + 1
            self.menu = self.parent.menu
        else:
            self.nesting_level = 0
        self.html_prefix = self.html_format()
        if self.menu:
            self.url = self.get_absolute_url()
        super(Category, self).save(force_insert, **kwargs)

    def html_format(self):
        return '&emsp;' * self.nesting_level * 2

    def get_absolute_url(self):
        return reverse(
            'items_view', args=[
                slugify(self.menu.title), str(self.slug)
            ]
        )

    def __str__(self):
        if self.menu:
            if self.parent:
                return (
                    f'Меню "{self.menu.title.capitalize()}": '
                    f'{self.title} (Родитель: {self.parent.title})'
                )
            return (
                f'Меню "{self.menu.title.capitalize()}": '
                f'{self.title} (Корневой каталог)'
            )
        return self.title


class Menu(models.Model):
    """Объект меню."""
    title = models.SlugField(
        verbose_name=_('Menu name'),
    )

    def __str__(self):
        return self.title
