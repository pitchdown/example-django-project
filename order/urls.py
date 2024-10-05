from django.urls import path
from .views import list_orders, order_detail


urlpatterns = [
    path('orders', list_orders, name='list_orders'),
    path('order-detail', order_detail, name='order_detail'),
]