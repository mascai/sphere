from django.contrib import admin
from models import Club, Comment, Like, Image, Event
# Register your models here.
admin.site.register(Comment)
admin.site.register(Club)
admin.site.register(Like)
admin.site.register(Image)
admin.site.register(Event)