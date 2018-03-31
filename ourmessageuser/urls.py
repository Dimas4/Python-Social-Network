from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views
from home.views import send_msgs

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.home, name='home'),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
    url(r'^send/(?P<pk>\d+)/$', send_msgs, name='send_msg')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)