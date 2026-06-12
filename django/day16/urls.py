from . import views
from django.urls import path

urlpatterns = [
    path("",views.Createview16,name="cetform"),
    path("stable/",views.DiaplayView16,name="stable"),
    path('update/<int:id>/',views.UpdateView,name='stupdate')
]

