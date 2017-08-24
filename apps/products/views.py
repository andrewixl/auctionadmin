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
    products = Product.objects.filter(owner = request.session['user_id']).all().order_by("product_end_date")
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
    return redirect("/")

def allproducts(request, view_id):
	products = None
	print view_id
	if view_id == "1":
		#Recently Created
		products = Product.objects.all().order_by("-created_at")
	elif view_id == "2":
		#Lowest Cost
		products = Product.objects.all().order_by("product_starting_bid")
	elif view_id == "3":
		#Highest Cost
		products = Product.objects.all().order_by("-product_starting_bid")
	elif view_id == "4":
		#Ending Soon
		products = Product.objects.all().order_by("product_end_date")
	productArr = []
	for product in products:
		dict={
		"id":product.id,
		"photo":product.photo,
		"product_name":product.product_name,
		"product_starting_bid":str(product.product_starting_bid),
		"created_at":str(product.created_at),
		"product_end_date":str(product.product_end_date),
		"product_description":product.product_description,
		"owner":product.owner.username,
		}
		productArr.append(dict)
	data = json.dumps(productArr)
	return HttpResponse(data, content_type='json')

def profile(request):
	try:
		request.session['user_id']
	except KeyError:
		return redirect("/login")
	context = {
	"first": request.session['first_name'],
	"last": request.session['last_name'],
	"username": request.session['username'],
	"email": request.session['email'],
	"city": request.session['city'],
	"state": request.session['state'],
	"phone": request.session['phone'],
	}
	return render(request, 'products/profile.html', context)

def deleteproduct(request, product_id):
	product = Product.objects.get(id = product_id).delete()
	return redirect('/')

def editproduct(request, product_id):
	product = Product.objects.get(id = product_id)
	context = {
		"product":product,
	}
	return render(request, 'products/editproduct.html', context)

def editproductdata(request,product_id):
	p = Product.objects.get(id = product_id)
	p.photo = request.POST['product_image']
	p.product_name = request.POST['product_name']
	p.product_starting_bid = request.POST['product_starting_bid']
	p.product_description = request.POST['product_description']
	p.save()
	return redirect('/')

def productdetails(request, product_id):
	product = Product.objects.get(id = product_id)
	dict={
	"id":product.id,
	"photo":product.photo,
	"product_name":product.product_name,
	"product_starting_bid":str(product.product_starting_bid),
	"created_at":str(product.created_at),
	"product_end_date":str(product.product_end_date),
	"product_description":product.product_description,
	"owner":product.owner.username,
	}
	data = json.dumps(dict)
	return HttpResponse(data, content_type='json')
