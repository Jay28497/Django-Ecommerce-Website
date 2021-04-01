from django.shortcuts import render
from .models.product import Product
from .models.category import Category


# Create your views here.
def index(request):
    categories = Category.get_all_categories()
    category_id = request.GET.get('category')

    if category_id:
        products = Product.get_all_products_by_category_id(category_id)
    else:
        products = Product.get_all_products()

    context = {'products': products, 'categories': categories}
    return render(request, 'store/index.html', context)
