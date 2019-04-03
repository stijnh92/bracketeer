from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import Group, User

from bracket.forms import BracketItemFormSet
from bracket.models import BracketItem
from nba.models import MatchUp


def index(request):
    bracket = BracketItem.objects.get_bracket()
    print(bracket)
    return render(request, 'bracket.html', bracket)


def group_list(request):
    groups = Group.objects.all()
    return render(request, 'groups.html', {'group_list': groups})


def group_detail(request, group_id):
    group = Group.objects.get(pk=group_id)
    return render(request, 'group_detail.html', {'group': group})


def bracket(request, user_id):
    user = User.objects.get(pk=user_id)
    bracket = BracketItem.objects.get_bracket(user)
    return render(request, 'bracket.html', bracket)


def leaderboard(request):
    return render(request, 'leaderboard.html')


def bracket_item(request):
    # if this is a POST request we need to process the form data
    match_up = MatchUp()

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form_set = BracketItemFormSet(request.POST, instance=match_up)

        print(request.POST)

        # check whether it's valid:
        if form_set.is_valid():
            print(form_set.cleaned_data)
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/bracket_item')

    # if a GET (or any other method) we'll create a blank form
    else:

        form_set = BracketItemFormSet(instance=match_up)

        print(form_set)

    return render(request, 'bracket_item.html', {
        'form_set': form_set
    })
