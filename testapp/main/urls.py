# coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
#from .views import hello

admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^hello/$', 'main.views.common', {"template_file": "hello.html"}),
    (r'^dojo/$', 'main.views.common', {"template_file": "dojo.html"}),
    (r'^center/$', 'main.views.common', {"template_file": "center.html"}),


)