from django.contrib import admin
from django.urls import path
from dto import views


urlpatterns = [
    #index 
    path("",views.index,name='dto'),
    #contact page
    path("contact",views.contact,name='contact'),
    #grevance page
    path("grievance",views.grievance,name='grievance'),

#challan urls for two,four,nongeared vehical and heavytrucks  
    path("two",views.two,name='two.html'),
    path("four",views.four,name='four.html'),
    path("nongear",views.nongear,name='nongear.html'),
    path("checknama",views.checknama,name='checknama.html'),
# authentication urls page
    path('register', views.registerPage, name="register"),
    path('login',views.loginPage, name="login"),
    path('logout',views.logoutUser, name="logout"),
#list views with filter urls of date and all gives the sum of all the challan amount collected 
    path("two_list",views.twos_list,name='two_list.html'),
    path("four_list",views.fours_list,name='four_list.html'),
    path("nongear_list",views.nongears_list,name='nongear_list.html'),
    path("all_list",views.alls_list,name='all_list.html'),
    path("check_list",views.check_list,name='check_list.html'),
 #search pages by registration number 
    path("search_two",views.searchs_two,name='search_two'),
    path("search_four",views.searchs_four,name='search_four'),
    path("search_nongear",views.searchs_nongear,name='search_nongear'),
    path("search_regno",views.searchs_regno,name='search_regno'),
    path("search_checknama",views.searchs_checknama,name='search_checknama'),
   
    path('user/',views.userPage,name='user-page'),
    
    path('sop',views.show_file,name='sop'),

    # path('news',views.news,name="news")

    
    

    

]

