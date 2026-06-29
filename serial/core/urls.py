from . import views
from django.urls import path

urlpatterns = [
    path('create/', views.create, name='create'),
    path('login/', views.login, name='login'),
    path('update/<int:id>/', views.update, name='update'),
]