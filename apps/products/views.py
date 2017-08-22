# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from ..login_app.models import User
from .models import Product
from django.core import serializers
from django.http import JsonResponse

def genErrors(request, Emessages):
	for message in Emessages:
		messages.error(request, message)

def index(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect("/login")
    photo = Product.objects.filter(owner = request.session['user_id']).all()
    print photo
    context = {
    'photos' : photo,
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
	data = serializers.serialize('json', products)
	return JsonResponse(data, safe=False)

# Create your views here.
