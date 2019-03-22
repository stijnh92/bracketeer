from django.shortcuts import render
from django.contrib.auth.models import Group, User


def index(request):
    return render(request, 'bracket.html')


def group_list(request):
    groups = Group.objects.all()
    return render(request, 'groups.html', {'group_list': groups})


def group_detail(request, group_id):
    group = Group.objects.get(pk=group_id)
    return render(request, 'group_detail.html', {'group': group})


def leaderboard(request):
    return render(request, 'leaderboard.html')
