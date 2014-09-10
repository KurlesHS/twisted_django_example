# coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
#from .views import hello

admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^hello/$', 'main.views.hello'),
    (r'^dojo/$', 'main.views.dojo'),

)