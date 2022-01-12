from tkinter import messagebox

from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import Booking,Places
from django.http import HttpResponse
# Create your views here.
def demo(request):
    return render(request,"index.html")
# def placedet(request):
#         # name=Places.objects.get('name')
#         # desc=Places.objects.get('desc')
#         place=Places()
#         return render(request,'place.html',{'place':place})
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('donate')
        else:
            messages.info(request,"Invalid User")
            return redirect('login')
    return render(request,'login.html')


def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Already Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                 messages.info(request,"Email Already Taken")
                 return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=first_name,email=email)

                user.save();
                messages.info(request,"Registration success")
        else:
            messages.info(request,"password not marching")
            return redirect('register')
        return redirect('donate')
    return render(request,'register.html')

def donate(request):

    return render(request,'donate.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
def fillform(request):
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        address=request.POST['address']
        bgroup=request.POST['bgroup']
        mob=request.POST['mob']

        booking=Booking(name=name,age=age,address=address,bgroup=bgroup,mob=mob)

        booking.save();
        messages.info(request,"Congratulations.Your Booking is Placed!")
    return render(request, 'form.html')


