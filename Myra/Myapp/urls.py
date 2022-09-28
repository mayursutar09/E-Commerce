from django.contrib import admin
from django.urls import path, include
from Myapp import views

urlpatterns = [
    path('',views.Middle,name='category'),
    path('contact/',views.contactview, name='contact'),
    path('products/',views.Products, name='products'),
    path('account/',views.Accountview, name='account'),
    path('about/',views.Aboutview, name='about'),
    path('details/<int:id>/',views.Detailsview, name='details'),
    path('cart/<int:id>/<int:quantity>/',views.Cartview, name='cart'),
    path('payment/',views.Payment, name='payment'),
    path('login/',views.Userlogin, name='login'),
    path('register/',views.Userregistration, name='register'),
    path('logout/',views.userlogout, name='logout'),

]
