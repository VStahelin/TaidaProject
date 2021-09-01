from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from Users.forms import RegisterForm


def registerPage(request):
    form = RegisterForm()
    context = {'form': form}

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
        else:
            for key, value in form.error_messages.items():
                print(value)
            context['error'] = value
            return render(request, 'users/Register.html', context)

    if request.user.is_authenticated:
        logout(request)
    return render(request, 'users/Register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('lists')
        else:
            messages.info(request, 'Username or password is incorrect')
            return render(request, 'users/Login.html')

    if request.user.is_authenticated:
        return redirect('lists')
    else:
        return render(request, 'users/Login.html')


def logoutPage(request):
    logout(request)
    return redirect('login')
