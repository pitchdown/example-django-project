from django.urls import path
from .views import products, popular_products


urlpatterns = [
    path('products', products, name='products'),
    path('popular-products', popular_products, name='popular_products'),
]