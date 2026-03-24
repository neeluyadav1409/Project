from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import Contacts
# Create your views here.
def index(request):
    return render(request,'index.html',{'titleName':"home"})

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        msg = request.POST.get("msg")
        c= Contacts(name=name,emailid=email,phone=phone,msg=msg)
        c.save()
    return render(request,'contact.html')

def product(request,name):
    print("hello ",name)
    return render(request,'product.html',{'name':name})
def login_view(request):
    return render(request,'login.html')
    if request.method == "POST":
     username=request.POST.get("Username")
     password=request.POST.get("Password")
    user = authenticate(username="john", password="secret")
    if user is not None:
     login(request, user)
    # A backend authenticated the credentials
     return redirect('/home')
    else:
    # No backend authenticated the credentials
     return redirect('login/',{'msg':"Invalid username or password"})                   
    return render(request,'login.html')
    
def signup_view(request):
    return render(request,'signup.html')
    if request.method == "POST":
        username=request.POST.get("Username")
        email=request.POST.get("Email")
        password=request.POST.get("Password")
        cpassword=request.POST.get("ConfirmPassword")
    if password == cpassword:
        user = User.objects.create_user("username", "email", "password")
        user.save()
        return redirect('/login')
    return render(request,'signup.html')
def logout_view(request):
    return redirect('/login')