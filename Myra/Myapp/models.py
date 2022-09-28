from django.db import models

# Create your models here.

class Image(models.Model):
    src =models.CharField(max_length=500)
    context=models.CharField(max_length=500,default="blank")
    price=models.CharField(max_length=50)
    cat1=models.CharField(max_length=50, default=None)
    cat2=models.CharField(max_length=50, default=None)
    cat3=models.CharField(max_length=50, default=None)
    cat4=models.CharField(max_length=50, default=None)
    productdetail=models.CharField(max_length=200, default=None)

class Testimonial(models.Model):
    para=models.CharField(max_length=500)
    src2=models.CharField(max_length=100)
    Name=models.CharField(max_length=10)

class Brands(models.Model):
    src3=models.CharField(max_length=100)

class Contact(models.Model):
    fullname=models.CharField(max_length=20)
    email=models.EmailField()
    mobile=models.CharField(max_length=20)
    message=models.CharField(max_length=100)

class MyraUser(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=15)