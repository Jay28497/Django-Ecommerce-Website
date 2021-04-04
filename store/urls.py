from django.urls import path
from .views.home import Index
from .views.login import Login, logout
from .views.signup import Signup
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('signup/', Signup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('cart/', Cart.as_view(), name='cart'),
    path('checkout/', CheckOut.as_view(), name='checkout'),
    path('orders/', OrderView.as_view(), name='orders'),
]
