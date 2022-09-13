from django.db import models

# Create your models here.

class Customer(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField()
	message=models.TextField()

	def __str__(self):
		return self.name


class Product(models.Model):
	product_image=models.ImageField(upload_to="product_image/")
	product_name=models.CharField(max_length=1000)


