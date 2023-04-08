from django.core import serializers
from django.http.response import HttpResponse, JsonResponse
from api.models import Product, Categories

categories = [
    {
        'id': 1, 
        'name': 'VR1',
    },
    {
        'id': 2, 
        'name': 'VR2',
    },
]
products = [
    {
        'id': 1, 
        'name': 'Helmet1',
        'category_name': 'VR1',
    },
    {
        'id': 2, 
        'name': 'Helmet2',
        'category_name': 'VR2',
    },
    {
        'id': 3, 
        'name': 'Helmet3',
        'category_name': 'VR1',
    },
]


def testGetProducts(request):
    products = serializers.serialize('json', Product.objects.all())
    return JsonResponse(products, safe = False)

def testGetProduct(request, id):
    products = Product.objects.all()
    for product in products:
        if(product['id'] == id):
            return JsonResponse(product, safe = False)
    return HttpResponse('No such product :(')

def testGetCategories(request):
    categories = serializers.serialize('json', Categories.objects.all())
    return JsonResponse(categories, safe = False)

def testGetCategory(request, id):
    categories = Categories.objects.all()
    for category in categories:
        if(category['id'] == id):
            return JsonResponse(category, safe = False)
    return HttpResponse('No such category :(')

def testGetProductByCategory(request, id):
    categories = Categories.objects.all()
    category = ""
    for c in categories:
        if(c['id'] == id):
            category = c
    
    products = Product.objects.all()
    productsByCategory = []
    for product in products:
        if(product['category_name'] == category['name']):
            productsByCategory.append(product)
    return JsonResponse(productsByCategory, safe = False)