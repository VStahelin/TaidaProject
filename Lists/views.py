from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from Anime.models import Anime
from Lists.forms import ListForm
from Lists.models import List


@login_required(login_url='login')
def createList(request):
    if request.method == 'POST':
        print(request.POST['type'])
        if request.POST['type'] == 'Anime':
            form = ListForm(request.POST)
            if form.is_valid():
                list = form.save(commit=False)
                list.user_owner = User.objects.get(id=request.user.id)
                list.save()

    return redirect(lists)


@login_required(login_url='login')
def lists(request):
    lists = List.objects.filter(user_owner=request.user.id)
    return render(request, 'lists/Lists.html', {'lists': lists})


@login_required(login_url='login')
def listDetails(request, id):
    list = List.objects.get(id=id)
    status = {'to_watch': 0,
              'watching': 0,
              'watched': 0}
    animes = []
    for anime in list.animes.all():
        anime_model = Anime.objects.get(id=anime.anime_id)

        studio = ''
        for a in anime_model.studios.all():
            studio = a.name
            break

        if anime.status == 'TW':
            status['to_watch'] += 1
        elif anime.status == 'WG':
            status['watching'] += 1
        elif anime.status == 'WD':
            status['watched'] += 1

        anime = anime.__dict__
        del anime['_state']
        anime['studio'] = studio
        anime['image_url'] = anime_model.image_url
        anime['mal_id'] = anime_model.mal_id
        anime['name'] = anime_model.name
        anime['episode'] = anime_model.episodes
        print(anime)
        animes.append(anime)
    return render(request, 'lists/ListDetails.html', {'list': list, 'animes': animes, 'status': status})
