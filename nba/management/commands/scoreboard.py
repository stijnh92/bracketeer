import requests

from django.core.management.base import BaseCommand, CommandError

from nba.models import MatchUp, Team


class Command(BaseCommand):
    help = 'Update the scores of the match ups.'

    def handle(self, *args, **options):
        match_ups = self.get_match_up_standings()

        for game in match_ups:
            try:
                match_up = MatchUp.objects.get(
                    home_team=game['home_team'],
                    away_team=game['away_team'],
                    user=None
                )

                match_up.home_score = game['home_score']
                match_up.away_score = game['away_score']
                match_up.save()
            except MatchUp.DoesNotExist:
                print(game)
                raise CommandError('Match up does not exist!')

    def get_match_up_standings(self):
        result = []

        self.stdout.write(self.style.SUCCESS('Fetching all games of today.'))
        scoreboard_url = 'http://data.nba.net/10s/prod/v1/20190414/scoreboard.json'

        request = requests.get(scoreboard_url)
        scoreboard = request.json()

        for game in scoreboard['games']:
            playoff_home = game['playoffs']['hTeam']
            playoff_away = game['playoffs']['vTeam']

            # Check which one of the teams is the lowest seed to determine the match up's home team.
            if playoff_home['seedNum'] < playoff_away['seedNum']:
                match_up_home_short = game['hTeam']['triCode']
                match_up_away_short = game['vTeam']['triCode']
            else:
                match_up_home_short = game['vTeam']['triCode']
                match_up_away_short = game['hTeam']['triCode']

            result.append({
                'home_team': Team.objects.get(short=match_up_home_short),
                'away_team': Team.objects.get(short=match_up_away_short),
                'home_score': playoff_home['seriesWin'],
                'away_score': playoff_away['seriesWin']
            })

        self.stdout.write(self.style.SUCCESS('Found %s games: ' % len(result)))
        for game in result:
            self.stdout.write('%s @ %s' % (game['away_team'], game['home_team']))

        return result