from django.urls import path
from . import views

urlpatterns = [
    path("",views.Home,name="home"),
    path("details/",views.Details,name="details"),
    path("single/<int:id>",views.Single,name="single")
]
