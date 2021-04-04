from django.shortcuts import render
from django.views import View
from store.models.orders import Order


class OrderView(View):
    def get(self, request):
        customer = request.session.get('customer_id')
        orders = Order.get_orders_by_customer(customer)
        # print(customer, orders)
        return render(request, 'store/orders.html', {'orders': orders})
