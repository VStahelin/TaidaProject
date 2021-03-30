from django.http import HttpResponse
from django.shortcuts import render, redirect


def dashboard(request):
    return render(request, 'main/Home.html')


def test(request):
    return render(request, 'main/Base.html')


def animeDetails(request):
    return render(request, 'anime/AnimeDetails.html')


def search(request):
    return render(request, 'main/Search.html')


def createList(request):
    return redirect('listDetails')


def lists(request):
    return render(request, 'lists/Lists.html')


def listDetails(request):
    return render(request, 'lists/ListDetails.html')
