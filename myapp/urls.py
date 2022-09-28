from django.urls import path
from .views import FirstView, SecondView

urlpatterns = [
    path('first/', FirstView.as_view()),
    path('second/', SecondView.as_view())
]