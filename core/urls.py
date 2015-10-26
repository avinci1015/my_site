from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^message/create/$', MessageCreateView.as_view(), name='message_create'),
    url(r'^success/$', Success.as_view(), name='success'),
    url(r'^about/$', AboutPage.as_view(), name='about_page'),
)