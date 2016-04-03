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

from importseasons import ImportSeasons
from season import Season
from team import Team
from os.path import expanduser

def getLeagueFromSeasons(seasons_list, league):
    Premiership = [x for x in seasons_list if x.isLeague(league)]
    return Premiership[0]

def main():
    seasons_list = []
    teams_list = []

    i = ImportSeasons()
    for s in i.importurlfromrest('http://api.football-data.org/v1/soccerseasons/?season=2015'):
        print s
        new_season = Season(s)
        seasons_list.append(new_season)

    pl = getLeagueFromSeasons(seasons_list, 'Premier League')

    teamsUrl = pl.getLinksUrl('teams')
    print 'teamsUrl=',teamsUrl
    teamsResponse = i.importurlfromrest(teamsUrl)
    for team in teamsResponse['teams']:
        new_team = Team(team)
        teams_list.append(new_team)

    PremiershipTeamNames = [x.getTeamAttr('name') for x in teams_list]
    PremiershipTeamShortNames = [x.getTeamAttr('shortName') for x in teams_list]
    PremiershipTeamSquadMarketValues = [x.getTeamAttr('squadMarketValue') for x in teams_list]
    table = zip(PremiershipTeamNames, PremiershipTeamShortNames, PremiershipTeamSquadMarketValues)
    for row in table:
        print row

    leagueTableUrl = pl.getLinksUrl('leagueTable')
    premiershipTable = i.importurlfromrest(leagueTableUrl)
    print 'premiershipTable length(',len(premiershipTable),') : ',premiershipTable
    print len(premiershipTable['standing'])
    standings = premiershipTable['standing']
    standings.sort(key=lambda x: x['points'], reverse=True)

    '''
    In a terminal, do
      grip ~/PycharmProjects/football/football/table.md
    Open safari at
      http://localhost:6419
    '''

    home = expanduser("~")
    path = '{0}/PycharmProjects/football/football/table.md'.format(home)
    with open(path, 'w') as f:
        f.write('| team | wins | draws | losses | points |\n')
        f.write('|---|---:|---:|---:|---:|\n')
        for j in standings:
            f.write('| {0} | {1} | {2} | {3} | {4} |\n'.format(j['teamName'], j['wins'], j['draws'], j['losses'], j['points']))
        f.close()

if __name__ == "__main__":
    main()
