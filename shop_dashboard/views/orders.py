from django.contrib.auth.hashers import check_password
from django.shortcuts import redirect, render
from django.views import View
from shop_dashboard.middlewares.auth import auth_middleware
from shop_dashboard.models.customer import Customer
from shop_dashboard.models.orders import Order
from shop_dashboard.models.product import Products


class OrderView(View):


    def get(self , request ):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request , 'orders.html'  , {'orders' : orders})
