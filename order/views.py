from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def list_orders(request):
    return JsonResponse({"order_ids": [1, 2, 4, 8]})


def order_detail(request):
    return JsonResponse({"order":
        [
            {
                "id": 1,
                'product_type': 'phone',
                "brand": "Apple",
                "name": "iPhone 13",
                "price": 1000
            },
            {
                "id": 7,
                'product_type': 'laptop',
                "brand": "Apple",
                "name": "MacBook Pro",
                "price": 2000
            }
        ]
    })
