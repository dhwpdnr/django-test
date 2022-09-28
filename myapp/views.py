from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

def hello_world(request):
    return HttpResponse("<h1>Hello world</h1>")

class FirstView(TemplateView):
    template_name = 'myapp/first.html'