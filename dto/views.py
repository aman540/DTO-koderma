
from django.contrib.auth import forms
from dto.models import Contact,Two,Four,Nongear
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime
from django.http import FileResponse
import io
# from reportlab.pdfgen import canvas
# from reportlab.lib.units import inch


from dto.forms import CreatUserForm



def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')
    

def contact(request):
    if request.method == "POST": 
         name = request.POST.get('name')
         phone  =request.POST.get('phone')
         email = request.POST.get('email')
         queries = request.POST.get('queries')
         contact = Contact( date=datetime.today(), name=name, phone=phone, email=email, queries=queries)
         contact.save()
         messages.success(request, 'We have recived your message,we will get to you soon.')
    return render (request,'contact/contact.html')           
    
#challan of vehicle

def two(request):  
    if request.method == "POST": 
         owner = request.POST.get('owner')
         regno  =request.POST.get('regno')
         chalantype = request.POST.get('chalantype')
         amt = request.POST.get('amt')
         
         two = Two( date=datetime.today(), owner=owner, regno=regno,  amt=amt, chalantype=chalantype)
         two.save()
         messages.success(request, ' CHALLAN DATA FOR TWO-WHEELER VEHICLE HAS BEEN RECORDED.')
    return render (request,'challan/two.html')  
   
def four(request):  
    if request.method == "POST": 
         owner = request.POST.get('owner')
         regno  =request.POST.get('regno')
         chalantype = request.POST.get('chalantype')
         amt = request.POST.get('amt')
         four = Four( date=datetime.today(), owner=owner, regno=regno,  amt=amt, chalantype=chalantype, )
         four.save()
         messages.success(request, ' CHALLAN DATA FOR FOUR-WHEELER VEHICLE HAS BEEN RECORDED.')
    return render (request,'challan/four.html')  
        
def nongear(request):  
    if request.method == "POST": 
         #datetime.today = request.POST.get('date')
         owner = request.POST.get('owner')
         regno  =request.POST.get('regno')
         chalantype = request.POST.get('chalantype')
         amt = request.POST.get('amt')
         nongear = Nongear( date=datetime.today(), owner=owner, regno=regno,  amt=amt, chalantype=chalantype)
         nongear.save()
         messages.success(request, ' CHALLAN DATA FOR NON-GEARED VEHICLE HAS BEEN RECORDED.')
    return render (request,'challan/nongear.html')  


#list pages with filters

def twos_list(request):
    two_list= Two.objects.all()
    nt=0
    for item in two_list:
       nt+=item.amt
    return render (request, 'list/two_list.html',{'two_list':two_list,'nt':nt})

def fours_list(request):
   four_list= Four.objects.all()
   nf=0
   for items in four_list:
       nf+=items.amt
   return render (request, 'list/four_list.html',{'four_list':four_list,'nf':nf})

def nongears_list(request):
   nongear_list= Nongear.objects.all()
   ns=0
   for itemss in nongear_list:
       ns+=itemss.amt
   return render (request, 'list/nongear_list.html',{'nongear_list':nongear_list,'ns':ns})  

def alls_list(request):
    if request.method =="POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        searchresult1 = Two.objects.filter(date__gte=fromdate, date__lte = todate)
        searchresult2 = Four.objects.filter(date__gte=fromdate, date__lte = todate)
        searchresult3 = Nongear.objects.filter(date__gte=fromdate, date__lte = todate)
        sum=0
        for item in searchresult1:
            sum+=item.amt 
        for item in searchresult2:
            sum+=item.amt 
        for item in searchresult3:
            sum+=item.amt
        return render(request,'list/all_list.html',{'displaydata1':searchresult1,'displaydata2':searchresult2,'displaydata3':searchresult3,'sum':sum})
    else:    
        displaydata1=Two.objects.all()
        displaydata2=Four.objects.all()
        displaydata3=Nongear.objects.all()
        sum1=0
        for item in displaydata1:
            sum1+=item.amt
        for item in displaydata2:
            sum1+=item.amt
        for item in displaydata3:
            sum1+=item.amt        
        return render(request,'list/all_list.html',{'displaydata1':displaydata1,'displaydata2':displaydata2,'displaydata3':displaydata3,'sum1':sum1})       
                 
#Search pages

def searchs_two(request):
    if request.method=="POST":
        twosearch = request.POST['twosearch']
        search_list4 = Two.objects.filter(regno__contains= twosearch)
        return render(request,'search_two.html',{'twosearch':twosearch, 'search_list4':search_list4,})
    else:
        return render(request,'search/search_two.html',{})

def searchs_four(request):
    if request.method=="POST":
        foursearch = request.POST['foursearch']
        search_list6 = Four.objects.filter(regno__contains= foursearch) 
        return render(request,'search_four.html',{'foursearch':foursearch, 'search_list6':search_list6 })
    else:
        return render(request,'search/search_four.html',{})           

def searchs_nongear(request):
    if request.method=="POST":
        nongearsearch = request.POST['nongearsearch']
        search_list5 = Nongear.objects.filter(regno__contains= nongearsearch)
        return render(request,'search_nongear.html',{'nongearsearch':nongearsearch, 'search_list5':search_list5})
    else:
        return render(request,'search/search_nongear.html',{})


#Authentication page
 

def registerPage(request):
    form=CreatUserForm()
    if request.method =='POST':
        form=CreatUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account has been created for ' + user)
            return redirect('login')
    context={'form':form}
    return render(request,'auth/register.html', context)        

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
    return render(request,'auth/login.html', context) 

def logoutUser(request):
    logout(request)
    return redirect('login')



