from django.urls import path
from . import views

urlpatterns = [
    path("",views.create),
    path("details/",views.details,name="details")
]
