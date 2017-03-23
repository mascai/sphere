from django.contrib import admin
from models import Club, Comment, Like, Image, Event
from model.models import UserProfile

admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Club)
admin.site.register(Like)
admin.site.register(Image)
admin.site.register(Event)