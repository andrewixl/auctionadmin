# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-24 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20170824_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_starting_bid',
            field=models.FloatField(max_length=300),
        ),
    ]