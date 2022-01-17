from django.shortcuts import render

from .models import PizzaModel as Product


def home_page(request):
    return render(request, 'homePage.html', {'products_list': Product.objects.all()})




