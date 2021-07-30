from django.contrib import admin
from django.urls import path
from dto import views

urlpatterns = [
    path("",views.index,name='dto'),
    path("contact",views.contact,name='contact'),

#challan urls  
  
    path("two",views.two,name='two.html'),
    path("four",views.four,name='four.html'),
    path("nongear",views.nongear,name='nongear.html'),

# authentication urls

    path('register', views.registerPage, name="register"),
    path('login',views.loginPage, name="login"),
    path('logout',views.logoutUser, name="logout"),

#list views with filter urls

    path("two_list",views.twos_list,name='two_list.html'),
    path("four_list",views.fours_list,name='four_list.html'),
    path("nongear_list",views.nongears_list,name='nongear_list.html'),
    path("all_list",views.alls_list,name='all_list.html'),

 #search pages  
    path("search_two",views.searchs_two,name='search_two'),
    path("search_four",views.searchs_four,name='search_four'),
    path("search_nongear",views.searchs_nongear,name='search_nongear'),
   
   
    
    
]
