#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sambopr.settings")

import django
django.setup()

from model.models import Club, Comment, Like
from django.utils import timezone

#Comment.objects.filter(author='Пользователь').delete()
Club.objects.filter(addr='Москва').delete()
Like.objects.all().delete()