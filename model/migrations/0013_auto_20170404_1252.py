# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0012_auto_20170404_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='club_logo',
            field=models.ImageField(blank=True, default=b'', upload_to=b'clubs/photos'),
        ),
    ]
