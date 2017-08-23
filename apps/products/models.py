# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login_app.models import User
from django.db import models


class ProductManager(models.Manager):
    def createProduct(self, postData, user_id):
        results = {'status': True, 'errors': [], 'user': None}
        if len(postData['product_name']) < 3:
            results['status'] = False
            results['errors'].append('Product Name Must be at Least 3 Characters.')
        if len(postData['product_image']) < 3:
            results['status'] = False
            results['errors'].append('URL Must be at Least 3 Characters.')
        if len(postData['product_starting_bid']) < 1:
            results['status'] = False
            results['errors'].append('Please Enter a Valid Starting Bid.')
        if len(postData['product_description']) < 10:
            results['status'] = False
            results['errors'].append(
                'Please Enter a Valid Product Description.')
        if len(postData['product_end_date']) < 3:
            results['status'] = False
            results['errors'].append(
                'Please Enter a Valid Product Description.')

        if results['status'] == True:
            results['errors'].append(
                'Your Product Has Successfully Been Added.')
            userInt = int(user_id)
            user = User.objects.get(id=userInt)
            results['person'] = Product.objects.create(photo=postData['product_image'], product_name=postData['product_name'], product_starting_bid=postData['product_starting_bid'],
                                                       product_end_date=postData['product_end_date'], product_description=postData['product_description'], owner=user)
        return results


class Product(models.Model):
    photo = models.CharField(max_length=1000)
    product_name = models.CharField(max_length=300)
    product_starting_bid = models.CharField(max_length=300)
    product_description = models.CharField(max_length=150)
    product_end_date = models.DateTimeField()
    owner = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ProductManager()

    def __str__(self):
        return self.product_name
# Create your models here.
