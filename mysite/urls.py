from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls import include, url
from django.contrib.auth import views
import django.contrib.auth.views
from django.conf.urls import include, url, patterns
admin.autodiscover()


urlpatterns = [
    # Examples:

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT
    }),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT
    }),
    url(r'^accounts/login/$', django.contrib.auth.views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('tiendas.urls')),

]
