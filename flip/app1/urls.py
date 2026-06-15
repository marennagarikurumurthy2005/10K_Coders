from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.product_list, name='product_list'),

    path(
        'cart/add/<int:product_id>/',
        views.add_to_cart,
        name='add_to_cart'
    ),

    path(
        'cart/',
        views.view_cart,
        name='view_cart'
    ),

    path(
        'purchase/',
        views.purchase,
        name='purchase'
    ),

    path(
        'cart/remove/<int:cart_id>/',
        views.remove_from_cart,
        name='remove_from_cart'
    ),
    
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )