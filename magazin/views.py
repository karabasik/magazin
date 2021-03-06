#-*- coding: utf8 -*-
from django.shortcuts import render_to_response, redirect
from .models import Product
from django.template.context_processors import csrf
from .forms import *



# Create your views here.


def products(request):
    return render_to_response('products.html', {'products': Product.objects.all()})


def product(request, product_id):
    args = {}
    args.update(csrf(request))
    args['product'] = Product.objects.get(id=product_id)
    return render_to_response('product.html', args)


def sort_phone(request):
    return render_to_response('phones.html', {'products': Product.objects.filter(type='phone')})


def smartphone(request):
    return render_to_response('smartphones.html', {'products': Product.objects.filter(type='smartphone')})


def tablets(request):
    return render_to_response('tablets.html', {'products': Product.objects.filter(type='tablet')})


def cart(request):
    Product.sum = -1
    return render_to_response('cart.html', {'products': Product.objects.all()})


