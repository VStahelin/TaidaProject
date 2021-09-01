from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from Anime.api.animeSearch import animeSearch
from Anime.api.manager import generateCardStructure


def home(request):
    return render(request, 'main/Home.html')


def test(request):
    return render(request, 'main/Base.html')


@login_required(login_url='login')
def search(request):
    if request.method == 'POST':
        search_field = request.POST['search_field']
        if request.POST['typeOptions'] == 'anime':
            list = generateCardStructure(animeSearch(search_field))
            return render(request, 'main/Search.html', {'result': list})

    return render(request, 'main/Search.html')
