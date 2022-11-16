from django.urls import path
from . import views  

urlpatterns=[
      
    path('',views.home, name='home'), 
    path('index',views.index, name='index'), 
    path('register',views.UserRegister, name = 'register'),
    path('adduser',views.adminUserRegister, name = 'adduser'), 
    path('login/',views.SignInView,name = 'login'),
    path('logout/',views.logout_view,name = 'logout'), 
    path('users/',views.User_list,name = 'user_list'),
    path('Users/<Prison_id>',views.Users,name = 'Users'),
    
    path('edit_user/<User_id>', views.edit_user, name='edit_user'),
    path('admin_edit_user/<User_id>', views.admin_edit_user, name='admin_edit_user'),
    path('deactivate_user/<User_id>', views.deactivate_user, name='deactivate_user'),
    path('activate_user/<User_id>', views.activate_user, name='activate_user'),
    
    path('region/',views.region,name='region'),
    
    path('criminal/',views.criminal, name='criminal'),
    
    path('criminal_list/',views.criminal_list,name='criminal_list'),
    path('ReleasedCriminal_list/',views.ReleasedCriminal_list,name='ReleasedCriminal_list'),
    path('edit_criminal/<Criminal_id>', views.edit_criminal, name='edit_criminal'),
    path('CriminalDetial/<Criminal_id>',views.CriminalDetial,name='CriminalDetial'),
    path('releaseCreminal/<Criminal_id>',views.releaseCriminal,name='releaseCriminal'),
    path('creminals/<Prison_id>',views.criminals,name='criminals'),
      
    # path('crime/',views.crime, name='crime'),
    # path('crime_list/',views.crime_list,name='crime_list'),
    # path('edit_crime/<Crime_id>', views.edit_crime, name='edit_crime'),
    
    path('prison/',views.prison, name='prison'),
    path('prison_list/',views.prison_list,name='prison_list'),
    path('edit_prison/<Prison_id>', views.edit_prison, name='edit_prison'),
     
    path('visitor/',views.visitor,name='visitor'),
    path('visitor_list/',views.visitor_list,name='visitor_list'),
    path('edit-visitor/<visitor_id>', views.edit_visitor, name='edit_visitor'),
    path('visitors/<Prison_id>',views.visitors,name='visitors'),
    


]