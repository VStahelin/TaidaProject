from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

from Lists.forms import ListForm
from Lists.models import List


@login_required(login_url='login')
def createList(request):
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            list = form.save(commit=False)
            list.user_owner = User.objects.get(id=request.user.id)
            list.save()

    return render(request, 'lists/Lists.html')


@login_required(login_url='login')
def lists(request):
    lists = List.objects.filter(user_owner=request.user.id)
    print(lists)
    return render(request, 'lists/Lists.html', {'lists': lists})


@login_required(login_url='login')
def listDetails(request):
    return render(request, 'lists/ListDetails.html')
