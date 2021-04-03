from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect

from Users.forms import RegisterForm


def register(request, **kwargs):
    form = RegisterForm()
    context = {'form': form}

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lists')
        else:
            for key, value in form.error_messages.items():
                print(value)
            context['error'] = value
            return render(request, 'users/Register.html', context)
    return render(request, 'users/Register.html', context)


def login(request):
    return render(request, 'users/Login.html')


def logout(request):
    return redirect('login')
