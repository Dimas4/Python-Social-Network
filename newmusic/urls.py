from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^mymusic/$', views.mymusic, name='mymusic'),
    url(r'^upload/$', views.Upload.as_view(), name='newmusic'),
    url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_files, name='change_files'),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)