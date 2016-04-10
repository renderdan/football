from os.path import expanduser

class ExportStandings():
    '''
    In a terminal, do e.g.
      grip ~/PycharmProjects/football/football/table.md
    Open browser at
      http://localhost:6419
    '''

    def __init__(self, md_path):
        home = expanduser("~")
        self.path = '{0}{1}'.format(home,md_path)

    def writeStandings(self, standings):
        with open(self.path, 'w') as f:
            f.write('| team | wins | draws | losses | points |\n')
            f.write('|---|---:|---:|---:|---:|\n')
            for row in standings:
                t = row['teamName'].encode('utf8')
                w = row['wins']
                d = row['draws']
                l = row['losses']
                p = row['points']
                f.write('| {0} | {1} | {2} | {3} | {4} |\n'.format(t,w,d,l,p))
            f.close()

    def writeFixtures(self, fixtures):
        with open(self.path, 'w') as f:
            f.write('| awayTeamName | homeTeamName | date | goalsAwayTeam | goalsHomeTeam |\n')
            f.write('|---|---:|---:|---:|---:|\n')
            for row in fixtures:
                t = row._response['awayTeamName'].encode('utf8')
                w = row._response['homeTeamName'].encode('utf8')
                d = row._response['date']
                l = row._response['result']['goalsAwayTeam']
                p = row._response['result']['goalsHomeTeam']
                f.write('| {0} | {1} | {2} | {3} | {4} |\n'.format(t,w,d,l,p))
            f.close()

    def writeTeams(self, teams):
        with open(self.path, 'w') as f:
            f.write('| awayTeamName | homeTeamName | date | goalsAwayTeam | goalsHomeTeam |\n')
            f.write('|---|---:|---:|---:|---:|\n')
            for row in teams:
                t = row._response['awayTeamName'].encode('utf8')
                w = row._response['homeTeamName'].encode('utf8')
                d = row._response['date']
                l = row._response['result']['goalsAwayTeam']
                p = row._response['result']['goalsHomeTeam']
                f.write('| {0} | {1} | {2} | {3} | {4} |\n'.format(t,w,d,l,p))
            f.close()
