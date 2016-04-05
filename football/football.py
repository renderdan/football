'''
    http://markdown-here.com

    wins : 19
    draws : 9
    home : {u'wins': 9, u'losses': 1, u'draws': 5, u'goals': 25, u'goalsAgainst': 15}
    playedGames : 31
    away : {u'wins': 10, u'losses': 2, u'draws': 4, u'goals': 29, u'goalsAgainst': 16}
    losses : 3
    teamName : Leicester City FC
    points : 66
    _links : {u'team': {u'href': u'http://api.football-data.org/v1/teams/338'}}
    goals : 54
    crestURI : http://upload.wikimedia.org/wikipedia/en/6/63/Leicester02.png
    position : 1
    goalDifference : 23
    goalsAgainst : 31
'''

from importdata import Import
from season import Season
from team import Team
from exportstandings import ExportStandings

def getLeagueFromSeasons(seasons_list, league):
    Premiership = [x for x in seasons_list if x.isLeague(league)]
    return Premiership[0]

def initializeSeasons(i):
    seasons_list = []
    for s in i.importurlfromrest('http://api.football-data.org/v1/soccerseasons/?season=2015'):
        print s
        new_season = Season(s)
        seasons_list.append(new_season)
    return seasons_list


def initializeTeams(i, league):
    teams_list = []
    teamsUrl = league.getLinksUrl('teams')
    print 'teamsUrl=',teamsUrl
    teamsResponse = i.importurlfromrest(teamsUrl)
    for team in teamsResponse['teams']:
        new_team = Team(team)
        teams_list.append(new_team)
    return teams_list


def getStandings(i, league):
    leagueTableUrl = league.getLinksUrl('leagueTable')
    premiershipTable = i.importurlfromrest(leagueTableUrl)
    print 'premiershipTable length(',len(premiershipTable),') : ',premiershipTable
    print len(premiershipTable['standing'])
    standings = premiershipTable['standing']
    standings.sort(key=lambda x: x['points'], reverse=True)
    return standings


def main():
    i = Import()
    seasons_list = initializeSeasons(i)
    pl = getLeagueFromSeasons(seasons_list, 'Premier League')
    teams_list = initializeTeams(i, pl)
    standings = getStandings(i, pl)
    exportstandings = ExportStandings()
    exportstandings.write(standings)

if __name__ == "__main__":
    main()
