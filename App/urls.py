"""Signup_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('',views.test, name='test'),
    
    path('api/signup/',views.signup, name='signup'),
    path('api/login/',views.login, name='login'),
    path('api/all-user-details/',views.allUserDetails, name='allUserDetails'),
    path('api/user-details/<slug:username>/', views.userDetails, name='userDetails'),
    path('api/edit-user-details/<slug:username>/',views.editUserDetails,name='editUserDetails'),
    path('api/delete-user-details/<slug:username>/',views.deleteUserDetails,name="deleteUserDetails"),
    
    # this api for  rendering frontpage as well as api directly
    path("single-function/signup/",views.singleFunctionSignup, name='singleFunctionSignup'),

    path('signup/', TemplateView.as_view(template_name='App/signup.html'), name='signuppage'),
    path('login/', TemplateView.as_view(template_name='App/login.html'), name='loginpage'),
    path('logout/', TemplateView.as_view(template_name='App/logout.html'), name='logoutpage'),

    path('home/', views.home, name='home'),
]
