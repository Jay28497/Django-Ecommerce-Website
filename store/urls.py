from django.urls import path
from .views.home import Index
from .views.login import Login, logout
from .views.signup import Signup

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('signup/', Signup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout, name='logout'),
]
