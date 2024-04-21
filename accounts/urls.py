from django.urls import re_path

from . import authentication

urlpatterns = [
    re_path('signup', authentication.signup),
    re_path('login', authentication.login),
    re_path('test_token', authentication.test_token),
]