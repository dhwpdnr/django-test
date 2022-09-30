from django.urls import path
from .apis import TodoCreateAPI, TodoDetailAPI, TodoUpdateAPI, TodoDeleteAPI
from .views import TodoCreateView

urlpatterns = [
    path('api/create/',TodoCreateAPI.as_view()),
    path('api/detail/<int:pk>',TodoDetailAPI.as_view()),
    path('api/update/<int:pk>',TodoUpdateAPI.as_view()),
    path('api/delete/<int:pk>',TodoDeleteAPI.as_view()),

    path('create/', TodoCreateView.as_view())
]