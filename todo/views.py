from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.

class TodoCreateView(APIView):
    def get(self, request):
        return render(request, "todo/create.html",{})
