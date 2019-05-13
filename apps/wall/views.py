from django.shortcuts import render, redirect
from apps.login_app.models import register
from .models import *
from django.contrib import messages

def dashboard(request):
#     print(messages.objects.get(id=1))
    context={
        "each": register.objects.get(id=request.session['id']),
        "messages": Messages.objects.all(),
        "comment": comments.objects.all(),
    }
    return render(request,'walls/dashboard.html', context)

def post(request):
    if request.method == "POST":
        this_user = register.objects.get(id=request.session['id'])
        this=Messages.objects.create(users=this_user, message=request.POST['message']),
        return redirect('/wall')


        
def delete(request, id):
        delete_mess=Messages.objects.get(id=id)
        print(delete_mess)
        delete_mess.delete()
        return redirect('/wall')

def hello(request,id):
        main_user=register.objects.get(id=request.session['id'])
        user=register.objects.get(id=id)
        context={
                "each": main_user,
                "messages": Messages.objects.filter(users=user),
                
        }
        return render(request,'walls/dashboard.html', context)

def edit(request,id):
        context={
                "user": register.objects.get(id=request.session['id']),
        }
        return render(request,'walls/edituser.html', context)
        
def save(request,id):
        errors = register.objects.account_validator(request.POST)
        if len(errors)>0:
                for key, value in errors.items():
                        messages.error(request,value)
                return redirect('/edit/'+id)
        else:
                c = register.objects.get(id=id)
                c.first_name = request.POST['first_name']
                c.last_name = request.POST['last_name']
                c.email = request.POST['email']
                c.save()
                return redirect('/wall')