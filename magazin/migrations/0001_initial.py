# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-18 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u041c\u043e\u0434\u0435\u043b\u044c \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430/\u043f\u043b\u0430\u043d\u0448\u0435\u0442\u0430')),
                ('price', models.CharField(max_length=50, verbose_name='\u0426\u0435\u043d\u0430')),
                ('sum', models.CharField(default='1', max_length=5, verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0432 \u043d\u0430\u043b\u0438\u0447\u0438\u0438')),
                ('inform', models.TextField(default='\u0422\u0435\u043a\u0441\u0442', verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430: \u041f\u0417\u0423,\u041e\u0417\u0423,\u0430\u0443\u0434\u0438\u043e \u0438 \u0442.\u0434')),
            ],
            options={
                'db_table': 'Product',
            },
        ),
    ]