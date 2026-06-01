from django.urls import path
from . import views

urlpatterns = [
    path('',views.Create, name="create"),
    path("details/",views.Details , name="details"),
    path("single/<int:id>/",views.Single , name="single"),
    path("delete/<int:id>/",views.Delete , name="delete"),
    path("update/<int:id>/",views.Update , name="update"),
]

