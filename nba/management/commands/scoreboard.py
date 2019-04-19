from datetime import date, timedelta
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

        today = date.strftime(date.today() - timedelta(1), '%Y%m%d')
        self.stdout.write(self.style.SUCCESS(f"Fetching all of yesterday's games..."))
        scoreboard_url = f'http://data.nba.net/10s/prod/v1/{today}/scoreboard.json'
        self.stdout.write(f'Using scoreboard URL {scoreboard_url}')

        request = requests.get(scoreboard_url)
        scoreboard = request.json()

        for game in scoreboard['games']:
            playoff_home = game['playoffs']['hTeam']
            playoff_away = game['playoffs']['vTeam']

            # Check which one of the teams is the lowest seed to determine the match up's home team.
            if playoff_home['seedNum'] < playoff_away['seedNum']:
                match_up_home_short = game['hTeam']['triCode']
                home_score = playoff_home['seriesWin']
                match_up_away_short = game['vTeam']['triCode']
                away_score = playoff_away['seriesWin']
            else:
                match_up_home_short = game['vTeam']['triCode']
                home_score = playoff_away['seriesWin']
                match_up_away_short = game['hTeam']['triCode']
                away_score = playoff_home['seriesWin']

            result.append({
                'home_team': Team.objects.get(short=match_up_home_short),
                'away_team': Team.objects.get(short=match_up_away_short),
                'home_score': home_score,
                'away_score': away_score
            })

        self.stdout.write(self.style.SUCCESS('Found %s games: ' % len(result)))
        for game in result:
            self.stdout.write(
                '%s @ %s (%s - %s)' % (
                    game['away_team'], game['home_team'],
                    game['home_score'], game['away_score']
                )
            )

        return result
