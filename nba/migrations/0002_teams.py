from django.db import migrations
from nba.models import Team


def load_all_teams(apps, schema_editor):
    teams = [
        ('Atlanta Hawks', 'ATL', 'ATL.svg'),
        ('Brooklyn Nets', 'BKN', 'BKN.svg'),
        ('Boston Celtics', 'BOS', 'BOS.svg'),
        ('Charlotte Hornets', 'CHA', 'CHA.svg'),
        ('Chicago Bulls', 'CHI', 'CHI.svg'),
        ('Cleveland Cavaliers', 'CLE', 'CLE.svg'),
        ('Dallas Mavericks', 'DAL', 'DAL.svg'),
        ('Denver Nuggets', 'DEN', 'DEN.svg'),
        ('Detroit Pistons', 'DET', 'DET.svg'),
        ('Golden State Warriors', 'GSW', 'GSW.svg'),
        ('Houston Rockets', 'HOU', 'HOU.svg'),
        ('Indiana Pacers', 'IND', 'IND.svg'),
        ('Los Angeles Clippers', 'LAC', 'LAC.svg'),
        ('Los Angeles Lakers', 'LAL', 'LAL.svg'),
        ('Memphis Grizzlies', 'MEM', 'MEM.svg'),
        ('Miami Heat', 'MIA', 'MIA.svg'),
        ('Milwaukee Bucks', 'MIL', 'MIL.svg'),
        ('Minnesota Timberwolves', 'MIN', 'MIN.svg'),
        ('New Orleans Pelicans', 'NOP', 'NOP.svg'),
        ('New York Knicks', 'NYK', 'NYK.svg'),
        ('Oklahama City Thunder', 'OKC', 'OKC.svg'),
        ('Orlando Magic', 'ORL', 'ORL.svg'),
        ('Philadelphia 76ers', 'PHI', 'PHI.svg'),
        ('Phoenix Suns', 'PHX', 'PHX.svg'),
        ('Portland Trail Blazers', 'POR', 'POR.svg'),
        ('Sacramento Kings', 'SAC', 'SAC.svg'),
        ('San Antonio Spurs', 'SAS', 'SAS.svg'),
        ('Toronto Raptors', 'TOR', 'TOR.svg'),
        ('Utah Jazz', 'UTA', 'UTA.svg'),
        ('Washington Wizards', 'WAS', 'WAS.svg')
    ]
    for team in teams:
        new_team = Team()
        new_team.name = team[0]
        new_team.short = team[1]
        new_team.logo = team[2]
        new_team.save()


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('nba', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_all_teams),
    ]
