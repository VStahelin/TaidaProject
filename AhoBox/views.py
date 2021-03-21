from django.http import HttpResponse
from django.shortcuts import render


def dashboard(request):
    return HttpResponse('<h1>AhoBox</h1>')


def test(request):
    return render(request, 'base.html')


def animeDetails(request):
    return render(request, 'AnimeDetails.html')
