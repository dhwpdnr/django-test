from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from rest_framework.views import APIView

# Create your views here.

def hello_world(request):
    return HttpResponse("<h1>Hello world</h1>")

class FirstView(TemplateView):
    template_name = 'myapp/first.html'

class SecondView(APIView):
    def get(self,request):
        user = "wpdnr"
        return render(request, "myapp/second.html",{"user" : user})