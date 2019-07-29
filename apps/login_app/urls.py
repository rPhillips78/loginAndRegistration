from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^display_login$', views.login_display),
    url(r'^success$', views.welcome),
    url(r'^logout$', views.logout)
]
