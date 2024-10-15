from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from .views import product_list, category_list, category_products, product_information, index
import debug_toolbar


urlpatterns = [
    path('', index, name='index'),
    path('category/', category_list, name='category_list'),
    path('category/<int:category_id>/products/', category_products, name='category_products'),
    path('products/', product_list, name='product_list'),
    path('product/<int:product_id>/', product_information, name='product_information')
]


if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

