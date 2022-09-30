from django.shortcuts import render
from rest_framework.views import APIView
from .models import Todo

# Create your views here.

class TodoCreateView(APIView):
    def get(self, request):
        return render(request, "todo/create.html",{})


class TodoListView(APIView):
    def get(self, request):
        todo_list = Todo.objects.all()
        return render(request, "todo/list.html", {"todo_list" : todo_list})


class TodoDetailView(APIView):
    def get(self, request,pk):
        todo = Todo.objects.filter(id = pk).first()
        return render(request, "todo/detail.html", {"todo": todo})


class TodoUpdateView(APIView):
    def get(self, request,pk):
        todo = Todo.objects.filter(id=pk).first()
        return render(request, "todo/update.html", {"todo": todo})