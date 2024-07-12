from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import newsletter
from .models import contact
from django.http import FileResponse
from django.conf import settings
import os
# Create your views here.
def index(request):
    if request.method =="POST":
        email=request.POST['email']
        news=newsletter(email=email)
        news.save()
        messages.success(request,'You are successfully added to newsletter!')
        return redirect('/')
    
    return render(request,'movieapp/index.html')

def about(request):
    return render(request,'movieapp/about.html')

def services(request):
    return render(request,'movieapp/services.html')

def find(request):
    return render(request,'movieapp/find.html')

def contact_us(request):
    if request.method =="POST":
        name=request.POST['name']
        email=request.POST['email']
        msg=request.POST['msg']
        con=contact(name=name,email=email,msg=msg)
        con.save()
        messages.success(request,'Your message has been sent!')
        return redirect('/contact')
        

    return render(request,'movieapp/contact.html')
