
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('prime/<int:num>',views.prime),
    path('login/<str:username>/<str:password>',views.login),
]
