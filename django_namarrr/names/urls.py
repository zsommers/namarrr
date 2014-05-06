from django.conf.urls import patterns, url

from names import views
from names.models import Adjective, Noun, Surname


urlpatterns = patterns(
    '',
    # Main page
    url(r'^$', views.index, name='index'),

    # Voting urls
    url(r'^adjectives/(?P<model_id>\d+)/upvote$',
        views.upvote,
        {'model': Adjective},
        name='adjective-upvote'),

    url(r'^adjectives/(?P<model_id>\d+)/downvote$',
        views.downvote,
        {'model': Adjective},
        name='adjective-downvote'),

    url(r'^nouns/(?P<model_id>\d+)/upvote$',
        views.upvote,
        {'model': Noun},
        name='noun-upvote'),

    url(r'^nouns/(?P<model_id>\d+)/downvote$',
        views.downvote,
        {'model': Noun},
        name='noun-downvote'),

    url(r'^surnames/(?P<model_id>\d+)/upvote$',
        views.upvote,
        {'model': Surname},
        name='surname-upvote'),

    url(r'^surnames/(?P<model_id>\d+)/downvote$',
        views.downvote,
        {'model': Surname},

        name='surname-downvote'),
)
