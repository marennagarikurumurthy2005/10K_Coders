from . import views
from django.urls import path

urlpatterns = [
    path('',views.create,name='create'),
    path('details/',views.details,name="details"),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('history/',views.history,name='history'),
    path('pd/<int:id>/',views.pd,name='pd'),
    path('retrive/<int:id>/',views.retrive,name='retrive')
]
