from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
#from model.views import add_like

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^model/register/$', views.register, name='register'),
    url(r'^model/login/$', views.user_login, name='login'),
    url(r'^model/logout/$', views.user_logout, name='logout'),
    url(r'^model/club_list/$', views.club_list, name='club_list'),
    url(r'^model/event_list/$', views.event_list, name='event_list'),
    url(r'^(?P<club_id>\d+)/$', views.club_detail, name='post'),
    #url(r'^(?P<slug>S+)/addlike/$', add_like, name='add_like'), #slug - from view.py


    #url(r'^model/club/$', views.user_logout, name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)