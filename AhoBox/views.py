from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'main/Home.html')


def test(request):
    return render(request, 'main/Base.html')


@login_required(login_url='login')
def animeDetails(request):
    return render(request, 'anime/AnimeDetails.html')


@login_required(login_url='login')
def search(request):
    return render(request, 'main/Search.html')


@login_required(login_url='login')
def createList(request):
    return redirect('listDetails')


@login_required(login_url='login')
def lists(request):
    return render(request, 'lists/Lists.html')


@login_required(login_url='login')
def listDetails(request):
    return render(request, 'lists/ListDetails.html')
