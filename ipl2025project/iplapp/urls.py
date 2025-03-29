
from django.contrib import admin
from django.urls import path
from iplapp.views import *
from . import views

app_name = 'iplapp' 

urlpatterns = [

    path('home/', views.home_view, name='home'),
    path('register/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('create/',create_view),
    path('display/',display_view),
    path('update/<int:n>/',update_view),
    path('delete/<int:n>/',delete_view),
]

# from django.urls import path


# urlpatterns = [
  
#     # other URLs
# ]

