# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-12-30 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='group',
            field=models.ManyToManyField(to='Web.UserGroup'),
        ),
    ]
