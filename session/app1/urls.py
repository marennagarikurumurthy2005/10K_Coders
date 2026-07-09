from django.urls import path
from . import views

urlpatterns = [
    # path('create/',views.create_session),
    # path('get/',views.get_session)

    path('send/',views.welcome)
    
]
