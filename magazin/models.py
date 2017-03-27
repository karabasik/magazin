#-*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models



choice_type = (
    ('phone', 'телефон'),
    ('smartphone', 'смартфон'),
    ('tablet', 'планшет'),
)


class Product(models.Model):
        class Meta():
            db_table = 'Product'
        stock = models.TextField(default='12 месяев гарантия при наличии чека', verbose_name='Скидки, акции , гарантии',)
        name = models.CharField(max_length=50, verbose_name='Модель телефона/планшета')
        price = models.CharField(max_length=50, verbose_name='Цена')
        sum = models.CharField(max_length=5, default='1', verbose_name='Количество в наличии')
        type = models.CharField(max_length=123, choices=choice_type)
        inform = models.TextField(default='Текст', verbose_name='Описание телефона: ПЗУ,ОЗУ,аудио и т.д')
        image = models.ImageField(blank=True, upload_to='images', help_text='250x500px', verbose_name='Image')
        def __str__(self):
            return self.name


class Buyer(models.Model):
        class Meta():
            db_table = 'Buyer'
        name = models.CharField(max_length=25, verbose_name='Фамилия Имя на английском')
        address = models.CharField(max_length=500, verbose_name='Адрес отправки')
        pochta = models.EmailField(default='exaple@example.com', max_length=300, verbose_name='Напишите почту')
        def __str__(self):
            return self.name