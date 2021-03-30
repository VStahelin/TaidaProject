from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect


def register(request):
    form = UserCreationForm()
    context = {'form':form}
    return render(request, 'users/Register.html', context)


def login(request):
    return render(request, 'users/Login.html')


def logout(request):
    return redirect('login')
