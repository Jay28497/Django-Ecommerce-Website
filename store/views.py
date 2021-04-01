from django.shortcuts import render
from .models.product import Product


# Create your views here.
def index(request):
    products = Product.get_all_products()
    return render(request, 'store/index.html', {'products': products})
