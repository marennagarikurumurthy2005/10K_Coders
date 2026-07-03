from . import views
from django.urls import path

urlpatterns = [
    path('create/',views.create),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.delete),
]
