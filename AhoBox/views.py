from django.http import HttpResponse
from django.shortcuts import render


def dashboard(request):
    return HttpResponse('<h1>AhoBox</h1>')


def test(request):
    return render(request, 'base.html')


def animeDetails(request):
    return render(request, 'AnimeDetails.html')


def search(request):
    return render(request, 'Search.html')


def createList(request):
    return render(request, 'CreateList.html')

def lists(request):
    return render(request, 'Lists.html')

def listDetails(request):
    return render(request, 'ListDetails.html')
