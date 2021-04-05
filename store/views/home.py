from django.shortcuts import render, redirect, HttpResponseRedirect
from store.models.product import Product
from store.models.category import Category
from django.views import View


class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {product: 1}

        request.session['cart'] = cart
        # print('cart', request.session['cart'])
        return redirect('index')

    def get(self, request):
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')


def store(request):
    # session clear cart
    # request.session.get('cart').clear()

    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}

    categories = Category.get_all_categories()
    category_id = request.GET.get('category')

    if category_id:
        products = Product.get_all_products_by_category_id(category_id)
    else:
        products = Product.get_all_products()

    context = {'products': products, 'categories': categories}
    # print("You are: ", request.session.get('customer_email'))
    return render(request, 'store/index.html', context)
