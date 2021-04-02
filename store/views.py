from django.shortcuts import render, redirect
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password


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


def validate_customer(customer):
    error_message = None

    if not customer.first_name:
        error_message = "First Name Required !!"
    elif len(customer.first_name) < 4:
        error_message = 'First Name must be 4 char long or more'
    elif not customer.last_name:
        error_message = 'Last Name Required !!'
    elif len(customer.last_name) < 4:
        error_message = 'Last Name must be 4 char long or more'
    elif not customer.mobile_no:
        error_message = 'Mobile Number required !!'
    elif len(customer.mobile_no) < 10:
        error_message = 'Mobile Number must be 10 char Long'
    elif len(customer.email) < 5:
        error_message = 'Email must be valid format and 5 char long !!'
    elif customer.email_exists():
        error_message = 'Email Address Already Registered..'
    elif len(customer.password) < 6:
        error_message = 'Password must be 6 char long !!'

    return error_message


def signup(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        mobile_no = request.POST.get('mobile_no')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # validation
        values = {
            'first_name': first_name,
            'last_name': last_name,
            'mobile_no': mobile_no,
            'email': email
        }

        error_message = None

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            mobile_no=mobile_no,
                            email=email,
                            password=password)
        error_message = validate_customer(customer)

        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('index')
        else:
            context = {
                'error': error_message,
                'value': values
            }
            return render(request, 'store/signup.html', context)
    else:
        return render(request, 'store/signup.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'store/login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')

        customer = Customer.get_customer_by_email(email)

        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                return redirect('index')
            else:
                error_message = "Email or Password invalid !!"
        else:
            error_message = "Email or Password invalid !!"

        return render(request, 'store/login.html', {'error': error_message})
