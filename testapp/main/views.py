# coding=utf-8
from django.template import loader, Context, TemplateDoesNotExist
from django.contrib.auth import authenticate, login as login_
import json
# Create your views here.
from django.http import HttpResponse


def common(request, template_file):
    print request.method
    print request.GET.dict()
    try:
        t = loader.get_template(template_file)
    except TemplateDoesNotExist:
        t = loader.get_template("blank.html")
    c = Context()
    return HttpResponse(t.render(c))


def login(request):
    print "user is auth: %s" % request.user.is_authenticated()
    print "username: %s" % request.user.username
    print request.method
    username = request.GET.get('login')
    password = request.GET.get('password')
    print username, password
    if username is not None and password is not None:
        response_data = dict()
        user = authenticate(username=username, password=password)
        result = 'failed'
        if user is not None:
            if user.is_active:
                result = 'success'
                login_(request, user)
            else:
                result = 'disabled'
        response_data['result'] = result
        response_data['message'] = 'Got message: ' + result

        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        t = loader.get_template("login.html")
        c = Context()
        return HttpResponse(t.render(c))