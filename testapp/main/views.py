# coding=utf-8
from django.shortcuts import render
import threading
# Create your views here.
from django.http import HttpResponse
from twisted.python import log


def hello(request):
    tid = threading.current_thread().ident
    log.msg("hello " + str(tid))
    return HttpResponse("Здравствуй, Мир")