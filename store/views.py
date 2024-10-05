from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def products(request):
    return JsonResponse({
        "products": {
            "phones": [
                {
                    "id": 1,
                    "brand": "Apple",
                    "name": "iPhone 13",
                    "price": 1000
                },
                {
                    "id": 2,
                    "brand": "Samsung",
                    "name": "Galaxy S21",
                    "price": 2000
                },
                {
                    "id": 3,
                    "brand": "Apple",
                    "name": "iPhone 12",
                    "price": 900
                },
                {
                    "id": 4,
                    "brand": "Samsung",
                    "name": "Galaxy S22",
                    "price": 2500
                },
                {
                    "id": 5,
                    "brand": "Apple",
                    "name": "iPhone 14",
                    "price": 1200
                },
                {
                    "id": 6,
                    "brand": "Samsung",
                    "name": "Galaxy S23",
                    "price": 3000
                }
            ],
            "laptops": [
                {
                    "id": 7,
                    "brand": "Apple",
                    "name": "MacBook Pro",
                    "price": 2000
                },
                {
                    "id": 8,
                    "brand": "Apple",
                    "name": "MacBook Air",
                    "price": 1500
                },
                {
                    "id": 9,
                    "brand": "Apple",
                    "name": "MacBook",
                    "price": 1000
                },
                {
                    "id": 10,
                    "brand": "Apple",
                    "name": "MacBook",
                    "price": 1000
                },
                {
                    "id": 11,
                    "brand": "Apple",
                    "name": "MacBook",
                    "price": 1000
                }
            ],
            "tablets": [
                {
                    "id": 12,
                    "brand": "Apple",
                    "name": "iPad",
                    "price": 500
                },
                {
                    "id": 13,
                    "brand": "Apple",
                    "name": "iPad",
                    "price": 500
                },
                {
                    "id": 14,
                    "brand": "Apple",
                    "name": "iPad",
                    "price": 500
                },
                {
                    "id": 15,
                    "brand": "Apple",
                    "name": "iPad",
                    "price": 500
                }
            ],
            "tvs": [
                {
                    "id": 16,
                    "brand": "Samsung",
                    "name": "Smart TV",
                    "price": 500
                },
                {
                    "id": 17,
                    "brand": "Samsung",
                    "name": "Smart TV",
                    "price": 500
                }
            ],
            "headphones": [
                {
                    "id": 18,
                    "brand": "Apple",
                    "name": "AirPods",
                    "price": 500
                },
                {
                    "id": 19,
                    "brand": "Apple",
                    "name": "AirPods",
                    "price": 500
                }
            ],
            "pcs": [
                {
                    "id": 20,
                    "brand": "Apple",
                    "name": "Mac",
                    "price": 500
                },
                {
                    "id": 21,
                    "brand": "Apple",
                    "name": "Mac",
                    "price": 500
                }
            ],
            "smartwatches": [
                {
                    "id": 22,
                    "brand": "Apple",
                    "name": "Apple Watch",
                    "price": 500
                },
                {
                    "id": 23,
                    "brand": "Apple",
                    "name": "Apple Watch",
                    "price": 500
                }
            ]
        }
    })


def popular_products(request):
    return JsonResponse({
        "popular_products": {
            "phones": [
                {
                    "id": 1,
                    "brand": "Apple",
                    "name": "iPhone 13",
                    "price": 1000
                },
                {
                    "id": 2,
                    "brand": "Samsung",
                    "name": "Galaxy S21",
                    "price": 2000
                }
            ],
            "laptops": [
                {
                    "id": 7,
                    "brand": "Apple",
                    "name": "MacBook Pro",
                    "price": 2000
                },
                {
                    "id": 8,
                    "brand": "Apple",
                    "name": "MacBook Air",
                    "price": 1500
                }
            ],
            "tablets": [
                {
                    "id": 12,
                    "brand": "Apple",
                    "name": "iPad",
                    "price": 500
                }
            ],
            "tvs": [
                {
                    "id": 16,
                    "brand": "Samsung",
                    "name": "Smart TV",
                    "price": 500
                }
            ],
            "headphones": [
                {
                    "id": 18,
                    "brand": "Apple",
                    "name": "AirPods",
                    "price": 500
                }
            ],
        }
    })
