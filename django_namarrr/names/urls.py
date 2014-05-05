from django.conf.urls import patterns, url

from names import views as views


urlpatterns = patterns(
    '',
    # Main page
    url(r'^$', views.index, name='index')
)
