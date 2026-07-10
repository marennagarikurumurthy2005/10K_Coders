from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.CreateView.as_view()),
]
