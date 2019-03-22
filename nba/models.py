from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=32)
    short = models.CharField(max_length=3)
    logo = models.CharField(max_length=10)


class MatchUp(models.Model):
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_team')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_team')
    home_score = models.IntegerField()
    away_score = models.IntegerField()
