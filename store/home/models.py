from django.db import models
# from cloudinary.models import CloudinaryField
# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=64, unique=True)
	slug = models.SlugField(max_length=64,unique=True)
	desc = models.TextField(max_length=150,null=True,blank=True)
	image = models.ImageField(upload_to='image')
	
	def __str__(self):
		return self.name


class BaseProducts(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='image')
    desc = models.TextField(max_length=150,null=True,blank=True)
    category = models.ForeignKey(Category,related_name='catlog',on_delete=models.CASCADE,default='')
    slug = models.ForeignKey(Category,related_name='sug',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Carousel(models.Model):
	name = models.CharField(max_length=64)
	desc = models.TextField(max_length=150,null=True,blank=True)
	image = models.ImageField(upload_to='image')

	def __str__(self):
		return self.name

class Contact(models.Model):
	Full_Name = models.CharField(max_length = 64)
	Phone_Number = models.IntegerField(null=False)
	Email_Address = models.EmailField()
	Subject = models.CharField(max_length=30)
	Message = models.TextField(max_length=250)

	def __str__(self):
		return f"Name:{self.Full_Name} - mobile:{self.Phone_Number}"