from django.shortcuts import render
from django.http import JsonResponse
from .models import Category, Product


# Create your views here.
def category_list(request):
    categories = Category.objects.filter()
    category_data = [
        {
            'id': category.id,
            'name': category.name,
            'children': [{'id': child.id, 'name': child.name} for child in category.children.all()]
        } for category in categories
    ]
    return JsonResponse({'categories': category_data})


def product_list(request):
    products = Product.objects.all()
    product_data = [
        {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'image': product.image.url if product.image else None,
            'categories': [{'id': category.id, 'name': category.name} for category in product.categories.all()]
        } for product in products
    ]
    return JsonResponse({'products': product_data})
