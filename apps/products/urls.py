from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^addproduct$', views.addproduct),
    url(r'^addproductdata$', views.addproductdata),
    url(r'^allproducts$', views.allproducts),
]
