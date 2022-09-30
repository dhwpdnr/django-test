from django.urls import path
from .apis import TodoCreateAPI, TodoDetailAPI, TodoUpdateAPI, TodoDeleteAPI
from .views import TodoCreateView, TodoListView, TodoDetailView, TodoUpdateView

app_name = "todo"

urlpatterns = [
    #API
    path('api/create/',TodoCreateAPI.as_view()),
    path('api/detail/<int:pk>',TodoDetailAPI.as_view()),
    path('api/update/<int:pk>',TodoUpdateAPI.as_view()),
    path('api/delete/<int:pk>',TodoDeleteAPI.as_view()),

    #VIEW
    path('create/', TodoCreateView.as_view()),
    path('list/', TodoListView.as_view(), name = "list"),
    path('detail/<int:pk>', TodoDetailView.as_view(), name="detail"),
    path('update/<int:pk>', TodoUpdateView.as_view(), name="update")
]