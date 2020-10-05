import json
import urllib

from django.shortcuts import render,get_object_or_404,redirect
from .models import BaseProducts,Category,Carousel
from .forms import ContactForm
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail


def home(request):
	category = Category.objects.all()
	carousel = Carousel.objects.all()
	context ={
		'category':category,
		'carousel':carousel,
	}
	return render(request,'home/home.html',context)

def about(request):
	return render(request,'home/about.html')

def franchise(request):
	return render(request,'home/franchise.html')

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['Full_Name']
			phone = form.cleaned_data['Phone_Number']
			sub = form.cleaned_data['Subject']
			email =form.cleaned_data['Email_Address']
			message= form.cleaned_data['Message']
			msg = "Name:%s\nPhone no:%s\nemail:%s\nSubject:%s\nMessage:%s"%(name,phone,email,sub,message)
			form_mail=settings.EMAIL_HOST_USER
			to_mail =settings.EMAIL_HOST_USER

			recaptcha_response = request.POST.get('g-recaptcha-response')
			url = 'https://www.google.com/recaptcha/api/siteverify'
			values = {
			    'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
			    'response': recaptcha_response
			}
			data = urllib.parse.urlencode(values).encode()
			req =  urllib.request.Request(url, data=data)
			response = urllib.request.urlopen(req)
			result = json.loads(response.read().decode()) 

			if result['success']:
			    form.save()
			    messages.success(request, 'Thank You for your Query.We will reply shortly ')
			    send_mail(sub,msg,form_mail,[to_mail])
			else:
			    messages.error(request, 'Invalid reCAPTCHA. Please try again.')

			return redirect('contact')
		
	form = ContactForm()
	return render(request,'home/contact.html',{'form':form})


def products(request):
	items = BaseProducts.objects.all()
	category = Category.objects.all()
	context ={
		'items':items,
		'category':category
	}
	return render(request,'home/products.html',context)

def product_list(request,slug):
	qs = get_object_or_404(Category,slug=slug)
	list_product = BaseProducts.objects.all().filter(category=qs.id)
	category = Category.objects.all()
	print(list_product)
	print(category)
	context={
		'category':category,
		'list_product':list_product,
	}
	return render(request,'home/products_details.html',context)
