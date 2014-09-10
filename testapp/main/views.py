# coding=utf-8
from django.template import loader, Context, TemplateDoesNotExist
# Create your views here.
from django.http import HttpResponse


def common(request, template_file):
    try:
        t = loader.get_template(template_file)
    except TemplateDoesNotExist:
        t = loader.get_template("blank.html")
    c = Context()
    return HttpResponse(t.render(c))