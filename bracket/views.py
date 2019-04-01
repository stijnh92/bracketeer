from django.shortcuts import render
from django.contrib.auth.models import Group, User

from bracket.models import BracketItem


def index(request):
    bracket = BracketItem.objects.get_master_bracket()
    return render(request, 'bracket.html', bracket)


def group_list(request):
    groups = Group.objects.all()
    return render(request, 'groups.html', {'group_list': groups})


def group_detail(request, group_id):
    group = Group.objects.get(pk=group_id)
    return render(request, 'group_detail.html', {'group': group})


def bracket(request, user_id):
    user = User.objects.get(pk=user_id)
    bracket = BracketItem.objects.get_user_bracket(user)
    return render(request, 'bracket.html', bracket)


def leaderboard(request):
    return render(request, 'leaderboard.html')
