import json

from django.template.defaulttags import register
from django.contrib.auth.forms import UserCreationForm
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import Group, User
from django.urls import reverse_lazy
from django.views import generic

from bracket.models import BracketItem


def index(request):
    bracket = BracketItem.objects.get_bracket()
    return render(request, 'bracket.html', bracket)


def group_list(request):
    groups = Group.objects.all()
    return render(request, 'groups.html', {'group_list': groups})


def group_detail(request, group_id):
    group = Group.objects.get(pk=group_id)
    users = group.user_set.all()

    for user in users:
        user.finals_match_up = None

        # Get the final bracket for this user.
        bracket_item = BracketItem.objects.get_item('1', 'M', user)

        if bracket_item.id and bracket_item.match_up:
            finals = bracket_item.match_up
            user.finals_match_up = {
                'winner': finals.get_winner(),
                'loser': finals.get_loser(),
                'games': finals.home_score + finals.away_score
            }

    return render(request, 'group_detail.html', {
        'group': group,
        'users': users
    })


def bracket(request, user_id):
    user = User.objects.get(pk=user_id)
    bracket = BracketItem.objects.get_bracket(user)
    bracket['edit_mode'] = request.GET.get('edit', False)
    bracket['bracket_user'] = user
    bracket['actual_bracket'] = get_flattened_master_bracket()

    return render(request, 'bracket.html', bracket)


def get_flattened_master_bracket():
    results = {}
    master_bracket = BracketItem.objects.get_bracket()

    for bracket_side, games_per_round in master_bracket.items():
        if bracket_side == 'final_bracket_item':
            final_game = games_per_round
            if final_game.id:
                results[final_game.side + str(final_game.index)] = final_game
        else:
            for games in games_per_round:
                for game in games:
                    if game.id:
                        results[game.side + str(game.index)] = game.match_up
    return results


def leaderboard(request):
    return render(request, 'leaderboard.html')


def save_bracket(request):
    data = json.loads(request.body)

    for key, match_up in data.items():
        BracketItem.objects.set_match_up(request.user, key[1], key[0], match_up)

    return JsonResponse({'status': 'OK'})


def create_group(request):
    try:
        Group.objects.create(name=request.POST['name'])
    except:
        print('Group could not be created!')
        print(request.POST)
    finally:
        return group_list(request)


def join_group(request, group_id):
    group = Group.objects.get(pk=group_id)
    group.user_set.add(request.user)

    return group_detail(request, group_id)


@receiver(post_save, sender=User)
def create_user_bracket(sender, instance, **kwargs):
    if kwargs.get('created', False):
        BracketItem.objects.create_new_bracket_for_user(instance)


class Register(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'


@register.filter
def get_item(dictionary, bracket_item):
    key = '%s%s' % (bracket_item.side, bracket_item.index)
    return dictionary.get(key)
