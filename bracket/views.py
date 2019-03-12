from django.shortcuts import render


def index(request):
    return render(request, 'bracket.html')


def groups(request):
    return render(request, 'groups.html')


def leaderboard(request):
    return render(request, 'leaderboard.html')
