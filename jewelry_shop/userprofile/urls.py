from django.contrib.auth import views as auth_views
from django.urls import path
from . import views



urlpatterns = [
   path('signup/', views.signup, name='signup'),
   path('login/', auth_views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),
   path('logout/', auth_views.LogoutView.as_view(), name='logout'),
   
    path('upload/', views.upload, name='upload'),
     path('upload/add-product/', views.add_product, name='add_product'),
   path('myaccount/', views.myaccount, name='myaccount'),
  
   
]
