from django.contrib.auth.models import User
from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=32)
    short = models.CharField(max_length=3)
    logo = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.short} ({self.name})'


class MatchUpManager(models.Manager):

    def get_or_create(self, game, user):
        home = game['home']
        away = game['away']

        home_team = Team.objects.get(short=home['team'])
        away_team = Team.objects.get(short=away['team'])

        try:
            match_up = self.model.objects.get(home_team=home_team, away_team=away_team, user=user)
            match_up.home_score = home['score']
            match_up.away_score = away['score']
            match_up.save()
            return match_up
        except MatchUp.DoesNotExist:
            match_up = self.model.objects.create(
                home_team=home_team,
                away_team=away_team,
                home_score=home['score'],
                away_score=away['score'],
                user=user
            )
            return match_up


class MatchUp(models.Model):
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_team')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_team')
    home_score = models.IntegerField(default=0)
    away_score = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def home_team_eliminated(self):
        return self.away_score == 4

    def home_team_advanced(self):
        return self.home_score == 4

    def away_team_eliminated(self):
        return self.home_score == 4

    def away_team_advanced(self):
        return self.away_score == 4

    objects = MatchUpManager()