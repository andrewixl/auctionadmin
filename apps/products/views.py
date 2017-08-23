# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings
from django.contrib import messages
from ..login_app.models import User
from .models import Product
from django.core import serializers
from django.http import JsonResponse
import json

def genErrors(request, Emessages):
	for message in Emessages:
		messages.error(request, message)

def index(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect("/login")
    products = Product.objects.filter(owner = request.session['user_id']).all()
    context = {
    'product' : products,
    }
    return render(request, 'products/index.html', context)

def addproduct(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect("/login")
    return render(request, 'products/addproduct.html')

def addproductdata(request):
    try:
		request.session['user_id']
		redirect("/")
    except KeyError:
		pass
    results = Product.objects.createProduct(request.POST, request.session['user_id'])
    request.session['productstatus'] = results['status']
    genErrors(request, results['errors'])
    return redirect("/addproduct")

def allproducts(request):
	products = Product.objects.all()
	productArr = []
	for product in products:
		dict={
		"id":product.id,
		"photo":product.photo,
		"product_name":product.product_name,
		"product_starting_bid":product.product_starting_bid,
		"created_at":str(product.created_at),
		"product_end_date":str(product.product_end_date),
		"product_description":product.product_description,
		"owner":product.owner.username,
		}
		productArr.append(dict)
	# return HttpResponse(productArr)
	data = json.dumps(productArr)
	# data = serializers.serialize('json', productArr)
	return HttpResponse(data, content_type='json')
	# return JsonResponse(data, safe=False)

# Create your views here.
