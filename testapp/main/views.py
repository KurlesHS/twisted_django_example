# coding=utf-8
from django.shortcuts import render
from django.template import loader, Context
import threading
# Create your views here.
from django.http import HttpResponse
from twisted.python import log


def hello(request):
    #tid = threading.current_thread().ident
    #log.msg("hello " + str(tid))
    #return HttpResponse("Здравствуй, Мир")
    t = loader.get_template('hello.html')
    c = Context()
    return HttpResponse(t.render(c))


def dojo(request):
    t = loader.get_template('dojo.html')
    c = Context()
    return HttpResponse(t.render(c))