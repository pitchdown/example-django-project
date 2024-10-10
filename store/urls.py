from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import product_list, category_list


urlpatterns = [
    path('categories/', category_list, name='category_list'),
    path('products/', product_list, name='product_list'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
