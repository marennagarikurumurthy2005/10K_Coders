
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('name/',views.name),
    path('num/',views.num),
    path('ads/',views.adds),
    path('branch/',views.branch),
    path('year/',views.year),
    path('father/',views.father),
    path('mother/',views.mother),
    path('sister/',views.sister),
    path('gp/',views.gp),
    path('details/',views.details),


]
