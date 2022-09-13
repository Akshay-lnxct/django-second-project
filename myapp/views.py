from django.shortcuts import render
from .models import Customer,Product

# Create your views here.

def index(request):
	products=Product.objects.all()
	return render(request,'index.html',{'products':products})


def contact_form(request):
	try:
		if request.method=="POST":
			Customer.objects.create(
				name=request.POST['name'],
				email=request.POST['email'],
				message=request.POST['message']
				)
	except:
		pass
	return render(request,'contact_form.html')