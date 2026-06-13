from django.urls import path
from . import views

urlpatterns = [

    path('',views.Formv,name="formv"),
    path('display/',views.Details,name="details"),
    path('update/<int:id>',views.Update,name="update"),
    path('delete/<int:id>',views.Delete,name="delete"),

    
]
