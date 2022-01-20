from django.shortcuts import render, redirect

from .cart import Cart
from .models import Customer, OrderList
from mainapp.models import PizzaModel as Product


def get_cart(request):
    final_set = []
    product_queryset = Product.objects.all()
    for product in Cart(request).cart.item_set.all():
        image = product_queryset.filter(id=product.object.id).first().image
        title = product_queryset.filter(id=product.object.id).first().title
        final_set.append([product, image,title])
    final_price = Cart(request).summary()
    return render(request, 'cartPage.html', {'cart': final_set, 'final_price': final_price})


def add_to_cart(request, **kwargs):
    product_id = kwargs.get('product_id')
    quantity = 1
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.add(product, quantity)
    return redirect('/')


def remove_from_cart(request, **kwargs):
    product_id = kwargs.get('product_id')
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(product)
    return redirect('/cart/')


def plus_1(request, **kwargs):
    product_id = kwargs.get('product_id')
    quantity = kwargs.get('quantity')
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.update(product, quantity + 1)
    return redirect('/cart/')


def minus_1(request, **kwargs):
    product_id = kwargs.get('product_id')
    quantity = kwargs.get('quantity')
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.update(product, quantity - 1)
    return redirect('/cart/')


def order(request):
    if 'customer_name' in request.POST \
            and 'customer_number' in request.POST \
            and 'customer_address' in request.POST \
            and request.POST['customer_number'].isdigit():

        customer = Customer.objects.filter(
            customer_name=request.POST['customer_name'],
            customer_number=request.POST['customer_number'],
            customer_address=request.POST['customer_address']
        )

        if Cart(request).cart.item_set.all().exists(): #vuln place
            if not customer.exists():
                customer = Customer(
                    customer_name=request.POST['customer_name'],
                    customer_number=request.POST['customer_number'],
                    customer_address=request.POST['customer_address']
                )
                customer.save()

            cart = Cart(request)
            if OrderList.objects.exists():
                last_order_id = OrderList.objects.last().order_id
            else:
                last_order_id = 0

            for item in cart.cart.item_set.all():
                item_for_order = OrderList(
                    order_id=last_order_id + 1,
                    customer=customer.first(),
                    product=item.object,
                    quantity=item.quantity
                )
                item_for_order.save()

    else:
        print('error')
        return redirect('/cart/', {'error': 'No customer data'})
    return orderAdd(request, customer)


def orderAdd(request, customer):
    cart = Cart(request)
    final_set = []
    product_queryset = Product.objects.all()
    for product in cart.cart.item_set.all():
        image = product_queryset.filter(id=product.object.id).first().image
        title = product_queryset.filter(id=product.object.id).first().title
        final_set.append([product, image, title])
    final_price = cart.summary()
    return render(request, 'orderAdd.html', {'cart': final_set,
                                             'final_price': final_price,
                                             'customer': customer.first()})


