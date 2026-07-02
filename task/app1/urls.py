from . import views
from django.urls import path

urlpatterns = [
    path('create/',views.create,name='create'),
    path('update/<int:id>/',views.update),
    path('delete/<int:id>/',views.delete),
    path('home/',views.home,name='home')
]
