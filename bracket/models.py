from django.contrib.auth.models import User
from django.db import models

from nba.models import MatchUp


class BracketManager(models.Manager):

    def get_master_bracket(self):
        games_left = [
            [self.model.objects.get(index=index, side='L', user=None) for index in range(1, 5)],
            [self.model(index=4, side='L'), self.model(index=5, side='L')],
            [self.model(index=6, side='L')],
        ]

        final_bracket_item = self.model(index=1, side='M')

        games_right = [
            [self.model(index=6, side='R')],
            [self.model(index=4, side='R'), self.model(index=5, side='R')],
            [self.model.objects.get(index=index, side='R', user=None) for index in range(1, 5)],
        ]

        return {
            'bracket_items_left': games_left,
            'bracket_items_right': games_right,
            'final_bracket_item': final_bracket_item
        }

    def get_user_bracket(self, user):
        return {}


class BracketItem(models.Model):
    match_up = models.ForeignKey(MatchUp, on_delete=models.CASCADE)
    side = models.CharField(max_length=1)
    index = models.IntegerField()
    points = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    objects = BracketManager()
