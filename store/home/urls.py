from django.urls import path
from .views import home,about,contact,franchise,products,product_list


urlpatterns=[
	path('',home,name='home'),
	path('about',about,name ='about'),
	path('contact',contact, name='contact'),
	path('products',products,name = 'products'),
	path('franchise',franchise,name = 'franchise'),
	path('product_list/<slug>',product_list,name = 'product_list'),
    ]