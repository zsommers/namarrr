from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout

from accounts import forms

urlpatterns = patterns(
    '',
    # Use custom template/form with builtin login
    url(r'^login$', login, {'template_name': 'accounts/login.html',
                            'authentication_form': forms.LoginForm,
                            'next_page': 'names:index',
                            },
        name='login'),
    # Redirect logouts back to main page
    url(r'^logout$', logout, {'next_page': 'names:index'}, name='logout'),
)
