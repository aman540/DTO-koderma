from django.contrib import admin
from django.urls import path
from dto import views

urlpatterns = [
    path("",views.index,name='dto'),
    path("apply",views.apply, name='apply'),
    path("contact",views.contact,name='contact'),
    path("two",views.two,name='two.html'),
    path("four",views.four,name='four.html'),
    path("nongear",views.nongear,name='nongear.html'),
    path('register', views.registerPage, name="register"),
    path('login',views.loginPage, name="login"),
    path('logout',views.logoutUser, name="logout"),
   
    
    
]
