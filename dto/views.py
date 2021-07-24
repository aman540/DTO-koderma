
from django.contrib.auth import forms
from dto.models import Contact,Two,Four,Nongear,Apply
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.forms import UserCreationForm

from dto.forms import CreatUserForm

# import pyrebase

# #For Firebase JS SDK v7.20.0 and later, measurementId is optional
# Config = {
#   "apiKey": "AIzaSyC5DDtRujQSHwBKSUAuQco09KR4YiP9g9s",
#   "authDomain": "dto-koderma.firebaseapp.com",
#   "projectId": "dto-koderma",
#   "storageBucket": "dto-koderma.appspot.com",
#   "messagingSenderId": "176939688122",
#   "appId": "1:176939688122:web:0f1f1812ab52372a1de283",
# }

# firebase = pyrebase.initialize_app(Config)
# authe = firebase.auth()
#datbase = firebase.database()


def index(request):
    if request.user.is_anonymous:
        return redirect("/login")

    return render(request,'index.html')

def apply(request):
    if request.method == "POST":
        name =request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        vtype = request.POST.get('vtype')
        gender = request.POST.get('gender')
        apply = Apply(name=name,  email=email, phone=phone, vtype=vtype, gender=gender)
        apply.save()
        messages.success(request, 'YOUR MESSAGE HAS BEEN SENT.')

    return render(request,'apply.html')   

def contact(request):
    if request.method == "POST": 
         name = request.POST.get('name')
         phone  =request.POST.get('phone')
         email = request.POST.get('email')
         queries = request.POST.get('queries')
         contact = Contact(name=name, phone=phone, email=email, queries=queries)
         contact.save()
         messages.success(request, 'YOUR MESSAGE HAS BEEN SENT.')
    return render (request,'contact.html')           
    
def two(request):  
    if request.method == "POST": 
         owner = request.POST.get('owner')
         regno  =request.POST.get('regno')
         chalantype = request.POST.get('chalantype')
         amt = request.POST.get('amt')
         city = request.POST.get('city')
         state = request.POST.get('state')
         zip = request.POST.get('zip')
         two = Two(owner=owner, regno=regno,  amt=amt, chalantype=chalantype, city=city, state=state, zip=zip)
         two.save()
         messages.success(request, 'DATA HAS BEEN RECORDED.')
    return render (request,'two.html')  

    

def four(request):  
    if request.method == "POST": 
         owner = request.POST.get('owner')
         regno  =request.POST.get('regno')
         chalantype = request.POST.get('chalantype')
         amt = request.POST.get('amt')
         city = request.POST.get('city')
         state = request.POST.get('state')
         zip = request.POST.get('zip')
         four = Four(owner=owner, regno=regno,  amt=amt, chalantype=chalantype, city=city, state=state, zip=zip)
         four.save()
         messages.success(request, 'DATA HAS BEEN RECORDED.')
    return render (request,'four.html')  
        

def nongear(request):  
    if request.method == "POST": 
         owner = request.POST.get('owner')
         regno  =request.POST.get('regno')
         chalantype = request.POST.get('chalantype')
         amt = request.POST.get('amt')
         city = request.POST.get('city')
         state = request.POST.get('state')
         zip = request.POST.get('zip')
         nongear = Nongear(owner=owner, regno=regno,  amt=amt, chalantype=chalantype, city=city, state=state, zip=zip)
         nongear.save()
         messages.success(request, 'DATA HAS BEEN RECORDED.')
    return render (request,'nongear.html')  
                 
       

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Password or Username is incorrect')
            

    context={}

    return render(request,'login.html', context) 

def logoutUser(request):
    logout(request)
    return redirect('login') 


def registerPage(request):

    form=CreatUserForm()

    if request.method =='POST':
        form=CreatUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'account was created for ' + user)
            return redirect('login')

    context={'form':form}
    return render(request,'register.html', context)        


