# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import User


class UserProfile(models.Model):
    # Эта строка обязательна. Она связывает UserProfile с экземпляром модели User.
    user = models.OneToOneField(User)

    # Дополнительные атрибуты, которые хотим добавить.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Переопределяем метод __unicode__(), чтобы вернуть что-либо значимое! Используйте __str__() в Python 3.*
    def __unicode__(self):
        return self.user.username

class Club(models.Model):
    title = models.CharField(max_length=50, db_index=True, default='Club') #name of the club
    addr = models.CharField(max_length=140, default='Москва')
    phone_number =  models.CharField(max_length=50, default='8-499-111-11-11')
    text = models.TextField(default='Информация о клубе') # text about the club
    coach_name = models.CharField(max_length=50, default='Харлампиев')
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __unicode__(self):
       return self.title
    
        
class Comment(models.Model):
    club = models.ForeignKey(Club)
    #author = models.CharField(max_length=200, default = 'Пользователь')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank = True,
        null = True
    )
    title = models.CharField(max_length=200, blank=True, null=True)
    text = models.CharField(max_length=200, default = 'Введите свой текст - комментарий') # comment text
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, 
            null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __unicode__(self):
        return unicode(self.text[:10]) 
        #created date в одну модель


class Like(models.Model):
	# ссылка на объект и кто лайкнул user -foreign
	#вместо автора - ссылка foreign на user
    #user = models.ForeignKey()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank = True,
        null = True
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null = True, blank = True)
    object_id = models.PositiveIntegerField(default=0, null = True, blank = True)
    content_object = GenericForeignKey('content_type', 'object_id')

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __unicode__(self):
       return 'Like ' + unicode(self.created_date)

class Image(models.Model):
    club = models.ForeignKey(Club)
    title = models.CharField(max_length=200)
    #number_of_photos = models.IntegerField(default=0)
    published_date = models.DateTimeField(blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __unicode__(self):
       return self.title

class Event(models.Model): #competition
    club = models.ForeignKey(Club)
    title = models.CharField(max_length=200)
    event_date = models.DateTimeField(db_index=True, blank=True, null=True)
    def publish(self):
        self.event_date = timezone.now()
        self.save()
    def __unicode__(self):
       return self.title    
    #события вывод db_index
    #row id fields