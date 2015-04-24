__author__ = 'harshit'

from django.conf.urls import patterns, include, url
from social import views

urlpatterns = patterns('',

    url(r'^$', views.home, name='home'),
    url(r'^userprofile/', views.profile, name='profile'),
)
