
from .decorators import unauthencated_user
from django.contrib.auth import forms
from .models import Contact,Two,Four,Nongear,Checknama,Grievance,FileUpload
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import Group,User
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime
from django.http import FileResponse
from .forms import CreatUserForm
from django.core.mail import send_mail
from django.conf import settings
from.decorators import unauthencated_user,allowed_users
import requests
from bs4 import BeautifulSoup
from rest_framework.decorators import api_view



def show_file(request):
    all_data=FileUpload.objects.all()

    context={'data':all_data}
    return render(request,'sop.html',context)

#INDEXPAGE

def index(request):
    if request.user.is_anonymous:
        return redirect("/login")

    url=f'https://newsapi.org/v2/top-headlines?country=in&apiKey=8d23f684b30346e9b902caca1550c665'
    r=requests.get(url)
    data=r.json()
    articles=data['articles']
    context={
        'articles':articles  }

    return render(request,'index/index.html',context)

#grivance page for user
def grievance(request):
    if request.method == "POST": 
         name = request.POST.get('name')
         phone  =request.POST.get('phone')
         email = request.POST.get('email')
         subject = request.POST.get('subject')
         file =request.POST.get('file')
         matter = request.POST.get('matter')
         grievance = Grievance( date=datetime.today(), name=name, phone=phone, email=email, subject=subject, file=file,matter=matter)
         grievance.save()
         messages.success(request, 'Your message has been sent to higher authoutity ,if found guilty action will be taken.')
         return render (request,'grievance.html',{'name':name})   
    else:
        return render (request,'grievance.html')
    
#CONTACT PAGE

@allowed_users(['admin','inspecter_incharge'])
def contact(request):
    if request.method == "POST": 
         name = request.POST.get('name')
         phone  =request.POST.get('phone')
         email = request.POST.get('email')
         queries = request.POST.get('queries')
         contact = Contact( date=datetime.today(), name=name, phone=phone, email=email, queries=queries)
         contact.save()

         messages.success(request, 'We have recived your message,we will get to you soon.')
         return render (request,'contact/contact.html',{'name':name})   
    else:
        return render (request,'contact/contact.html')

    
#CHECKNAKA CHALLAN INFORMATION
@allowed_users(allowed_roles=['admin','inspecter_incharge']) 
def checknama(request):
    if request.method == "POST": 
         name = request.POST.get('name')
         regno  =request.POST.get('regno')
         vt = request.POST.get('vt')
         chalanno = request.POST.get('chalanno')
         checknama = Checknama( date=datetime.today(), name=name, regno=regno,vt=vt,chalanno=chalanno)
         checknama.save()
         messages.success(request, 'Data has been recorded.')
    return render (request,'challan/checknama.html')    

#eCHALLAN RECORD ENTRY PAGE
#FOR TWOWHEELER
@allowed_users(allowed_roles=['admin','inspecter_incharge']) 
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
#FOR FOURWHEELER  
@allowed_users(allowed_roles=['admin','inspecter_incharge']) 
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
 # FOR NONGERAED VEHICAL
@allowed_users(allowed_roles=['admin','inspecter_incharge'])     
def nongear(request):  
    if request.method == "POST": 
         owner = request.POST.get('owner')
         regno  =request.POST.get('regno')
         chalantype = request.POST.get('chalantype')
         amt = request.POST.get('amt')
         nongear = Nongear( date=datetime.today(), owner=owner, regno=regno,  amt=amt, chalantype=chalantype)
         nongear.save()
         messages.success(request, ' CHALLAN DATA FOR NON-GEARED VEHICLE HAS BEEN RECORDED.')
    return render (request,'challan/nongear.html')  


#LIST AND VIEWS PAGE FOR ALL THE ENTRIES MADE IN E-CHALLAN SECTION

#FOR TWO WHEELER LIST ENTRIES WITH DATE AND SEARCH FILTER
@allowed_users(allowed_roles=['admin'])
def twos_list(request):
    if request.method =="POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        two_list = Two.objects.filter(date__gte=fromdate, date__lte = todate)
        nt=0
        for item in two_list:
            nt+=item.amt
        return render (request, 'list/two_list.html',{'twos_lists':two_list,'nt':nt})
    else:    
        twos_lists=Two.objects.all()
        nt1=0
        for item in twos_lists:
            nt1+=item.amt
        return render (request, 'list/two_list.html',{'twos_lists':twos_lists,'nt1':nt1})    
   
    
#FOR FOUR WHEELER LIST ENTRY WITH DATE AND SEARCH FILTER
@allowed_users(allowed_roles=['admin'])
def fours_list(request):
    if request.method =="POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        four_list = Four.objects.filter(date__gte=fromdate, date__lte = todate)
        nf=0
        for item in four_list:
            nf+=item.amt
        return render (request, 'list/four_list.html',{'fours_lists':four_list,'nf':nf})
    else:    
        fours_lists=Four.objects.all()
        nf1=0
        for item in fours_lists:
            nf1+=item.amt
        return render (request, 'list/four_list.html',{'fours_lists':fours_lists,'nf1':nf1}) 
#FOR NONGERAED VEHICLE ENTRIES LIST WITH DATE AND SEARCH FILTER
@allowed_users(allowed_roles=['admin'])
def nongears_list(request):
    if request.method =="POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        nongear_list = Nongear.objects.filter(date__gte=fromdate, date__lte = todate)
        nn=0
        for item in nongear_list:
            nn+=item.amt
        return render (request, 'list/nongear_list.html',{'nongears_lists':nongear_list,'nn':nn})
    else:    
        nongears_lists=Nongear.objects.all()
        nn1=0
        for item in nongears_lists:
            nn1+=item.amt
        return render (request, 'list/nongear_list.html',{'nongears_lists':nongears_lists,'nn1':nn1})   

#FOR HEAVY VEHICAL WITH DATE AND SEARCH FILTER
@allowed_users(allowed_roles=['admin'])
def check_list(request):
    if request.method =="POST":          
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        checks_list = Checknama.objects.filter(date__gte=fromdate, date__lte = todate)
        return render (request, 'list/check_list.html',{'checks_lists':checks_list})
        
    else:   
        checks_lists=Checknama.objects.all()
        return render (request, 'list/check_list.html',{'checks_lists':checks_lists})  

        
 # ALL VEHICAL LIST WITH DATE AND SEARCH FILTER CACLULATING SUM  
@allowed_users(allowed_roles=['admin'])
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
        displaydata1=Two.objects.order_by('-date')
        displaydata2=Four.objects.order_by('-date')
        displaydata3=Nongear.objects.order_by('-date')
        sum1=0
        for item in displaydata1:
            sum1+=item.amt
        for item in displaydata2:
            sum1+=item.amt
        for item in displaydata3:
            sum1+=item.amt        
        return render(request,'list/all_list.html',{'displaydata1':displaydata1,'displaydata2':displaydata2,'displaydata3':displaydata3,'sum1':sum1})       
                 
#Search pages

#SEARCH REGISTRATION NUMBER OF TWO WHEELER
@allowed_users(allowed_roles=['admin'])
def searchs_two(request):
    if request.method=="POST":
        twosearch = request.POST['twosearch']
        search_list4 = Two.objects.filter(regno__contains= twosearch).reverse()
        return render(request,'list/nongear_list.html',{'twosearch':twosearch, 'search_list4':search_list4,})
    else:
        return render(request,'list/nongear_list.html',{})
#SEARCH REGISTRATION NO OF FOUR WHEELER
@allowed_users(allowed_roles=['admin'])
def searchs_four(request):
    if request.method=="POST":
        foursearch = request.POST['foursearch']
        search_list6 = Four.objects.filter(regno__contains= foursearch)
        return render(request,'search/search_four.html',{'foursearch':foursearch, 'search_list6': search_list6})
    else:
        return render(request,'search/search_nongear.html',{})       
#SEARCH REGISTRATION NO OF NONGEARED VEHICLE
@allowed_users(allowed_roles=['admin'])
def searchs_nongear(request):
    if request.method=="POST":
        nongearsearch = request.POST['nongearsearch']
        search_list5 = Nongear.objects.filter(regno__contains= nongearsearch)
        return render(request,'search/search_nongear.html',{'nongearsearch':nongearsearch, 'search_list5': search_list5})
    else:
        return render(request,'search/search_nongear.html',{})
#SEARCH ALL VEHICAL BY REGISTRATION NO
@allowed_users(allowed_roles=['admin'])
def searchs_regno(request):
    if request.method =="POST":
        searched = request.POST["searched"]
        search_list1 = Two.objects.filter(regno__contains=searched)
        search_list2 = Four.objects.filter(regno__contains=searched)
        search_list3 = Nongear.objects.filter(regno__contains=searched)
        return render(request,'search/search_regno.html',{'searched':searched, 'search_list1':search_list1,'search_list2':search_list2,'search_list3':search_list3})
    else:
         return render(request,'search/search_regno.html',{})
#SEARCH REGISTRATION NO OF BIG VEHICLE
@allowed_users(allowed_roles=['admin'])
def searchs_checknama(request):
    if request.method=="POST":
        checknamasearch = request.POST['checknamasearch']
        search_list11 = Checknama.objects.filter(regno__contains= checknamasearch)
        return render(request,'search/search_checknama.html',{'checknamasearch':checknamasearch, 'search_list11':search_list11,})
    else:
        return render(request,'search/search_checknama.html',{})             
#Authentication page
 
#USER REGISTRATION PAGE FOR SIGNUP
@unauthencated_user
def registerPage(request):
    form=CreatUserForm()
    if request.method =='POST':
        form=CreatUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username = form.cleaned_data.get('username')
            group= Group.objects.get(name='customer')
            user.groups.add(group)

            messages.success(request,'Account has been created for ' + username)
            return redirect('login')
    context={'form':form}
    return render(request,'auth/register.html', context)        
#USER LOGIN PAGE FOR LOGIN
@unauthencated_user
def loginPage(request):
    if request.method ==  'POST':
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
#LOGOUT PAGE
def logoutUser(request):
    logout(request)
    return redirect('login')


def userPage(request):
    context = {}
    return render(request,'user.html',context)


def news(request):
    url=f'https://newsapi.org/v2/top-headlines?country=in&apiKey=8d23f684b30346e9b902caca1550c665'
    r=requests.get(url)
    data=r.json()
    articles=data['articles']
    context={
        'articles':articles
    }
    return render(request,'news.html',context)
    

