# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-02 09:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0015_auto_20170411_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(default=b'\xd0\x92\xd0\xb2\xd0\xb5\xd0\xb4\xd0\xb8\xd1\x82\xd0\xb5 \xd1\x81\xd0\xb2\xd0\xbe\xd0\xb9 \xd1\x82\xd0\xb5\xd0\xba\xd1\x81\xd1\x82 - \xd0\xba\xd0\xbe\xd0\xbc\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0\xd1\x80\xd0\xb8\xd0\xb9'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
