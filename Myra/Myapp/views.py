from multiprocessing import context
from django.forms import PasswordInput
from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User

# Create your views here.

def Middle(request):
    Variable1=Image.objects.all().values()
    Variable2=Testimonial.objects.all().values()
    Variable3=Brands.objects.all().values()
    context ={
        "src":[],
        "src2":[],
        "src3":[],
    }
    for i in Variable1:
        context["src"].append(i)
    for i in Variable2:
        context["src2"].append(i)
    for i in Variable3:
        context["src3"].append(i)
    return render(request,'middle.html',context)

def contactview(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        message=request.POST.get('message')
        user=Contact(fullname=name,email=email,mobile=mobile,message=message)
        user.save()
        # messages.success(request, 'Your message has been sent successfully.')
    return render(request, "contact.html")

def Products(request):
    Variable=Image.objects.all().values()
    context ={
        "src2":[],
    }
    for i in Variable:
        context["src2"].append(i)
    return render(request,'product.html',context)

def Accountview(request):
    return render(request,'account.html')

def Userlogin(request):
    if request.method=="POST":
        username=request.POST.get("user")
        password=request.POST.get("pass")
        userObj=authenticate(request,username=username,password=password)
        if userObj is not None:
            login(request,userObj)
            return redirect('/')
        else:
            return render(request,'account.html')

def Userregistration(request):
    if request.method=="POST":
        username=request.POST.get("user")
        email=request.POST.get("email")
        password=request.POST.get("pass")
        userObj=authenticate(request,username=username,password=password)
        if userObj is not None:
            login(request,userObj)
            return redirect('/')
        else:
          User.objects.create_user(username,email,password)
          return render(request,'account.html')
    else:
        return render(request,'account.html')

def userlogout(request):
    logout(request)
    return redirect('/')

def Aboutview(request):
    return render(request,'about.html')

def Detailsview(request,id):
    vardetails=Image.objects.filter(id=id)[0]
    context={
        "vardetails":vardetails
    }
    return render(request, 'detals.html',context)

def Cartview(request,id,quantity):
    cartdetail=Image.objects.filter(id=id)[0]
    context={
        "cartdetail":cartdetail,
        "quantity":quantity
    }
    return render(request, 'cart.html',context)

def Payment(request):
    return render(request, 'payment.html')