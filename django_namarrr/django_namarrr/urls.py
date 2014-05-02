# from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'django_namarrr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

# if settings.DEBUG:
#     import debug_toolbar
#     print("DEBUG=True - Importing debug_toolbar")
#     urlpatterns += patterns(
#         '',
#         url(r'^__debug__/', include(debug_toolbar.urls)),
#     )
