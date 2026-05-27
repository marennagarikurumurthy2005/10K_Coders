from . import views
from django.urls import path

urlpatterns = [
    path("",views.Home),
    path("display/",views.Display,name="display")
]
