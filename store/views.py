from itertools import product
from multiprocessing import context
from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime

from .models import *

# Create your views here.

def store(request):
    products = Product.objects.all()
    context={
        'products':products,
    }
    return render(request, 'store/index.html', context)

def cart(request):
    context={}
    return render(request, 'store/cart.html', context)


def checkout(request):
    
    context={}
    return render(request, 'store/checkout.html', context)



