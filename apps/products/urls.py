from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^addproduct$', views.addproduct),
    url(r'^addproductdata$', views.addproductdata),
    url(r'^allproducts$', views.allproducts),
    url(r'^profile$', views.profile),
    url(r'^delete/(?P<product_id>\d+)$', views.deleteproduct),
    url(r'^edit/(?P<product_id>\d+)$', views.editproduct),
    url(r'^editproductdata/(?P<product_id>\d+)$', views.editproductdata),
]
