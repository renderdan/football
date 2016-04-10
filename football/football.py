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
from response import Response
from exportstandings import ExportStandings
from os.path import expanduser

class Football:
    def __init__(self, token):
        print 'foo'
        self.token = token


    def dump_league_names(self, label, attr, list):
        print label
        for leagueName in [x._response[attr] for x in list]:
            print '"',leagueName,'"'

    def getLeagueFromSeasons(self, seasons_list, league):
        Premiership = [x for x in seasons_list if x.isLeague(league)]
        return Premiership[0]

    def initializeSeasons(self, i):
        seasons_list = []
        for s in i.importurlfromrest('http://api.football-data.org/v1/soccerseasons/?season=2015'):
            print s
            new_season = Season(s)
            seasons_list.append(new_season)
        return seasons_list


    def initializeTeams(self, i, league):
        teams_list = []
        teamsUrl = league.getLinksUrl('teams')
        print 'teamsUrl=',teamsUrl
        teamsResponse = i.importurlfromrest(teamsUrl)
        for team in teamsResponse['teams']:
            new_team = Team(team)
            teams_list.append(new_team)
        return teams_list


    def initializeFixtures(self, i, league):
        fixtures_list = []
        url = league.getLinksUrl('fixtures')
        print 'fixturesUrl=',url
        response = i.importurlfromrest(url)
        for fixture in response['fixtures']:
            new_fixture = Response(fixture)
            fixtures_list.append(new_fixture)
        return fixtures_list


    def getStandings(self, i, league, sort_by):
        leagueTableUrl = league.getLinksUrl('leagueTable')
        premiershipTable = i.importurlfromrest(leagueTableUrl)
        print 'premiershipTable length(',len(premiershipTable),') : ',premiershipTable
        print len(premiershipTable['standing'])
        standings = premiershipTable['standing']
        standings.sort(key=lambda x: x[sort_by], reverse=True)
        return standings


def main():
    '''
    In a terminal, do
      grip ~/PycharmProjects/football/football/table.md
    Open browser at
      http://localhost:6419
    '''
    token = None
    token_path = '{0}{1}'.format(expanduser("~"),'/PycharmProjects/football/football/auth_token.txt')
    with open(token_path, 'r') as f:
        token = f.read().rstrip()

    league_names = ['Premier League', 'League One', 'Champions League', '1. Bundesliga', '2. Bundesliga']
    football = Football(token)
    i = Import(football.token)
    seasons_list = football.initializeSeasons(i)
    football.dump_league_names('League Names : ', 'caption', seasons_list)
    pl = football.getLeagueFromSeasons(seasons_list, league_names[0])
    teams = football.initializeTeams(i, pl)
    fixtures = football.initializeFixtures(i, pl)
    standings = football.getStandings(i, pl, sort_by='points')

    ExportStandings('/PycharmProjects/football/football/table.md').writeStandings(standings)
    ExportStandings('/PycharmProjects/football/football/fixtures.md').writeFixtures(fixtures)
    #ExportStandings('/PycharmProjects/football/football/teams.md').writeTeams(teams)

if __name__ == "__main__":
    main()
