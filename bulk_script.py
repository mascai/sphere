#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import uuid
import random
#import pymysqlclient
import MySQLdb
import random

#pymysql.install_as_MySQLdb()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sambopr.settings")

import django
django.setup()

from model.models import Club, Comment, Like, Event, Image
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.conf import settings

try:
    AMOUNT = int(sys.argv[1])
except:
    AMOUNT = 100000

def create_random_Club():
    data = []
    for i in range(1, AMOUNT+1):
        data.append({
            'id': i, #не желательно
            #'title':  'scriptClub' + unicode(i)
            'title': 'Sambo ' + unicode(random.randint(1920, 2017))
            #'text': 'Club random text' 
            })

    return data

def set_Data():

    Club.objects.all().delete()
    data = create_random_Club()
    objs = [Club(**d)  for d in data]
    Club.objects.bulk_create(objs)
    #достать club_id
    comm_arr = []
    event_arr = []
    imag_arr = []
    like_arr = []
    i = 1
    for q in objs:
        comm_arr.append(Comment(club = q, text = unicode(i) + 'qweqw'))
        event_arr.append(Event(club = q, title = 'Event ' + unicode(i)))
        imag_arr.append(Image(club = q, title = 'Imag ' + unicode(i)))
        like_arr.append(Like())
        i += 1
    Comment.objects.bulk_create(comm_arr)
    Event.objects.bulk_create(event_arr)
    Image.objects.bulk_create(imag_arr)
    Like.objects.bulk_create(like_arr)


if __name__ == '__main__':
    set_Data()