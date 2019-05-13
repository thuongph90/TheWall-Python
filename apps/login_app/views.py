from django.shortcuts import render,redirect
import bcrypt
from .models import *
from django.contrib import messages

def index(request):
     return render(request,"login/homepage.html")

def registor(request):
    print(request.POST)
    errors = register.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/')
    else:
        if request.method=="POST":
            if register.objects.filter(email=request.POST['email']):
                messages.error(request, "email already exists.")
                return redirect('/')
            else:
                hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
                one=register.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],password=hash1)
                # print(one)
                request.session['id']=one.id
                return redirect('/wall')

def success(request):
    context = {
        "one": register.objects.get(id=request.session['id'])
        }
    return render(request,"login/success.html", context)

def loginaccount(request):
    # I try to make an if statement to check email from login input exits in the database??
    if not register.objects.filter(email=request.POST['email']):
        messages.error(request, "email no exist.")
        return redirect('/')
    else:
        user = register.objects.get(email=request.POST['email'])
        print(user.email)
        if bcrypt.checkpw(request.POST['password'].encode(),user.password.encode()):
            request.session['id']=user.id
            return redirect('/wall')
        else:
            messages.error(request, "password failed.")
            print("failed password")
            return redirect('/')
    
def logout(request):
    request.session.clear()
    return redirect('/')


