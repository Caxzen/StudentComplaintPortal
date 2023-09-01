from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from . import views
from .models import Student
from django import forms


#myuser = User.objects.create_user(username='ajay',password='123')
#myuser.save()


def login(request):
    return render(request,"authentication/login.html")

def home(request):
    posts = Student.objects.all()
    args = {'posts':posts}
    if request.method == 'POST':
        username1 = request.POST['regno']
        pass1 = request.POST['pass']
        #user = authenticate(username=username1,password=pass1)
        
        if username1=='ajay' and pass1=='123':
            login(request)
            return render(request,"authentication/home.html",args)
        else:
            
            return render(request,"authentication/login.html")
    else:
        return render(request,"authentication/home.html",args)

def post(request):
    if request.method == 'POST':
        posts = Student.objects.all()
        new1 = Student()
        new1.name = request.POST['name']
        new1.title = request.POST['title']
        new1.content = request.POST['complaint']
        new1.save()
        args = {'posts':posts}


        return render(request,"authentication/home.html",args)
    else:
        return render(request,"authentication/post.html")
    

