from django.urls import path
from . import views

urlpatterns = [
    path('',views.Create),
    path('dis/',views.Display,name='display')
]
