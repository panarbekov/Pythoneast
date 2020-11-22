from django.urls import path
from .views import *

urlpatterns = [
    path("", homepage, name="home"),
    path("signin/", authorization, name="login"),
    path("signout/", signout, name="logout"),
    path("registration/", registration, name="registration")
]