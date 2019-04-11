from django.contrib.auth.models import User
from django.db import models

from nba.models import MatchUp


class BracketManager(models.Manager):

    def create_new_bracket_for_user(self, user):
        master_bracket_items = self.get_master_bracket_items()
        for bracket_item in master_bracket_items:
            match_up = bracket_item.match_up
            match_up.pk = None
            match_up.user = user
            match_up.save()

            bracket_item.pk = None
            bracket_item.user = user
            bracket_item.match_up = match_up
            bracket_item.save()

    def get_master_bracket_items(self):
        return [self.get_item(index, side) for index in range(1, 5) for side in ['L', 'R']]

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
            return self.model(index=index, side=side, user=user)

    def set_match_up(self, user, bracket_side, bracket_index, game):
        bracket_item = self.get_item(bracket_side, bracket_index, user)
        match_up = MatchUp.objects.get_or_create(game, user)
        bracket_item.match_up = match_up
        bracket_item.save()


class BracketItem(models.Model):
    match_up = models.ForeignKey(MatchUp, on_delete=models.CASCADE)
    side = models.CharField(max_length=1)
    index = models.IntegerField()
    points = models.IntegerField(default=0)
    finished = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    base_points = 10
    bonus_points = 5

    def get_max_points(self):
        max_points = self.base_points + self.bonus_points
        if self.side == 'F':
            return max_points * 8

        if self.index in (1, 2, 3, 4):
            return max_points
        if self.index in (5, 6):
            return max_points * 2
        elif self.index == 7:
            return max_points * 4

    def get_min_points(self):
        if self.side == 'F':
            return self.base_points * 8

        if self.index in (1, 2, 3, 4):
            return self.base_points
        if self.index in (5, 6):
            return self.base_points * 2
        elif self.index == 7:
            return self.base_points * 4

    objects = BracketManager()
