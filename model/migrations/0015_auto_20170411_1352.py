# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-11 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0014_auto_20170404_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='title',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
