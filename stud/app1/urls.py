from . import views
from django.urls import path

urlpatterns = [
    path('register/',views.register),
    path('login/',views.login),
    path('home/',views.home),
    path('logout/',views.logout),
    path('add/',views.add_student),
    path('delete/<int:id>/',views.delete_student),
    path('update/<int:id>/',views.update_student),
]
