# from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    # Built-in Admin
    url(r'^admin/', include(admin.site.urls)),
    # User interactions
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    # Main name app
    url(r'^$', include('names.urls', namespace='names')),
)
