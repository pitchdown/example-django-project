from django.shortcuts import render
from django.http import JsonResponse
from .models import Category, Product
from django.db.models import F, Avg, Sum


# Create your views here.
def index(request):
    return render(request, 'index.html')


def category_list(request):
    categories = Category.objects.filter(parent=None)
    return render(request, 'category.html', {'categories': categories})


def category_products(request, category_id):
    category = Category.objects.get(id=category_id)
    products = category.products.prefetch_related('categories')
    products_with_total_price = products.annotate(total_price=F('price') * F('quantity'))
    most_expensive_product = products.order_by('-price').first()
    cheapest_product = products.order_by('price').first()
    avg_price = products.aggregate(avg_price=Avg('price'))
    total_products_cost = 0
    for product in products:
        total_products_cost += product.price*product.quantity
    return render(request, 'category_products.html', {'category': category, 'products': products_with_total_price,
                                                      'most_expensive_product': most_expensive_product, 'cheapest_product': cheapest_product,
                                                      'avg_price': avg_price['avg_price'], 'total_products_cost': total_products_cost})


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


def product_information(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product.html', {'product': product})
