# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-12-31 15:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0005_auto_20171231_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publish_date',
            field=models.DateTimeField(auto_now=True, verbose_name='\u53d1\u5e03\u65e5\u671f'),
        ),
    ]
