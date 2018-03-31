from django.conf.urls import url, include
from django.contrib import admin
from tutorial import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.login_redirect, name='login_redirect'),
    url(r'^music/', include('newmusic.urls', namespace='music')),
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('accounts.urls', namespace='accounts')),
    url(r'^home/', include('home.urls', namespace='home')),
    url(r'^messages/', include('ourmessageuser.urls', namespace='ourmessageuser')),
    url(r'^chat/', include('chat.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)