from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('Register', views.registerPage, name='register'),
    path('Login', views.loginPage, name='login'),
    path('Logout', views.logoutPage, name='logout')
]
