from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from Anime.api.animeSearch import animeSearch


def home(request):
    return render(request, 'main/Home.html')


def test(request):
    return render(request, 'main/Base.html')


@login_required(login_url='login')
def animeDetails(request):
    return render(request, 'anime/AnimeDetails.html')


@login_required(login_url='login')
def search(request):
    if request.method == 'POST':
        search_field = request.POST['search_field']
        if request.POST['typeOptions'] == 'anime':
            list = animeSearch(search_field)
            return render(request, 'main/Search.html', {'result': list})
        else:
            pass

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
