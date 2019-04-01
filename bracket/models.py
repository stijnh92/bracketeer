from django.contrib.auth.models import User
from django.db import models

from nba.models import MatchUp


class BracketManager(models.Manager):

    def get_bracket(self, user=None):
        return {
            'bracket_items_left': self.get_side_bracket('L', user),
            'bracket_items_right': self.get_side_bracket('R', user, True),
            'final_bracket_item': self.get_item(1, 'M', user)
        }

    def get_side_bracket(self, side, user, reverse=False):
        side_bracket = [
            [self.get_item(index, side, user) for index in range(1, 5)],
            [self.get_item(5, side, user), self.get_item(6, side, user)],
            [self.get_item(7, side, user)]
        ]
        if reverse:
            side_bracket.reverse()

        return side_bracket

    def get_item(self, index, side, user=None):
        try:
            return self.model.objects.get(index=index, side=side, user=user)
        except BracketItem.DoesNotExist:
            return self.model(index=index, side=side)


class BracketItem(models.Model):
    match_up = models.ForeignKey(MatchUp, on_delete=models.CASCADE)
    side = models.CharField(max_length=1)
    index = models.IntegerField()
    points = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    objects = BracketManager()
