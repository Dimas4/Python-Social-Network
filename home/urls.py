from django.conf.urls import url
from home.views import HomeView
from . import views

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_friends, name='change_friends'),
    url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_friends_user, name='change_friends_user'),
    url(r'^send/(?P<pk>\d+)/$', views.send_msg, name='send_msg'),
    url(r'^users/$', views.users.as_view(), name='users'),
    url(r'^allmessage/$', views.allmessage, name='allmessage'),
    url(r'^allmessage_global/$', views.allmessage_global, name='allmessage_global'),
    url(r'^friend/$', views.friend.as_view(), name='friend'),
]
