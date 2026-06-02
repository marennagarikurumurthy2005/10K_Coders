"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('data/',include('day1.urls')),
    path('day2/',include('day2.urls')),
    path('templates/',include('day3.urls')),
    path('day4/',include('day4.urls')),
    path('day5/',include('day5.urls')),
    path('day6/',include('day6.urls')),
    path('day7/',include('day7.urls')),
    path('day8',include('day8.urls')),
    path('day9/',include('day9.urls')),
    path('day10/',include('day10.urls')),
    path('day11/',include('day11.urls')),
    path('day12/',include('day12.urls')),
    path('day13/',include('day13.urls')),
    # path('',views.home),
    # path('name/',views.name),
    # path('num/',views.num),
    # path('ads/',views.adds),
    # path('branch/',views.branch),
    # path('year/',views.year),
    # path('father/',views.father),
    # path('mother/',views.mother),
    # path('sister/',views.sister),
    # path('gp/',views.gp),
    # path('details/',views.details),

]
