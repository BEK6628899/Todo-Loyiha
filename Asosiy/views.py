from django.shortcuts import render,redirect
from .models import *
from django.views import View
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User




def Loginview(request):
    if request.method == "POST":
        user = authenticate(username=request.POST.get('l'),           # user.objects.filter()
                     password=request.POST.get('p'))
        if user is None:                                               # if len(user) == 0:
            return redirect('/')
        login(request, user)
        return redirect('/todo')
    return render(request,"login.html")



def Logaut(request):
    logout(request)
    return redirect('/')



def todo(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            Todo.objects.create(
                plan = request.POST.get('reja'),
                time = request.POST.get('vaqt'),
                description = request.POST.get('tavsif'),
                status = request.POST.get('status')
            )
        data = {"todos":Todo.objects.filter(foydalanuvchi=request.user)}
        return render(request,"todo.html",data)
    return redirect('/')



def ochirish(request,son):
    a = Todo.objects.get(id=son)
    if a.foydalanuvchi == request.user:
        a.delete()
    return redirect("/todo")



def register(request):
    if request.method == 'POST' and request.POST.get('p') == request.POST.get('cp'):
        User.objects.create_user(
            username=request.POST.get('l'),
            password=request.POST.get('cp')
        )
        return redirect('/')
    return render(request,"register.html")



