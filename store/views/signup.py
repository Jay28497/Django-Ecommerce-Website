from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'store/signup.html')

    def post(self, request):
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
        error_message = self.validate_customer(customer)

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

    def validate_customer(self, customer):
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
