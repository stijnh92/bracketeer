from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=32)
    short = models.CharField(max_length=3)
    logo = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.short} ({self.name})'


class MatchUp(models.Model):
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_team')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_team')
    home_score = models.IntegerField(default=0)
    away_score = models.IntegerField(default=0)

    def home_team_eliminated(self):
        return self.away_score == 4

    def home_team_advanced(self):
        return self.home_score == 4

    def away_team_eliminated(self):
        return self.home_score == 4

    def away_team_advanced(self):
        return self.away_score == 4
