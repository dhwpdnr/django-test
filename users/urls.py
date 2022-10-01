from django.urls import path
from .apis import SignupAPI, LoginAPI
from .views import SignupView, LoginView

app_name = 'users'

urlpatterns=[
    path("api/signup/", SignupAPI.as_view()),
    path("signup/", SignupView.as_view()),

    path("api/login/", LoginAPI.as_view()),
    path("login/", LoginView.as_view()),
]
