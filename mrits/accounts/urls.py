from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import CusomTokenObtainView

urlpatterns = [
    path('login/',CusomTokenObtainView.as_view()),
    path('refresh/',TokenRefreshView.as_view()),
]

