from os.path import expanduser

class ExportStandings():
    '''
    In a terminal, do
      grip ~/PycharmProjects/football/football/table.md
    Open browser at
      http://localhost:6419
    '''

    def __init__(self):
        home = expanduser("~")
        self.path = '{0}/PycharmProjects/football/football/table.md'.format(home)

    def write(self, standings):
        with open(self.path, 'w') as f:
            f.write('| team | wins | draws | losses | points |\n')
            f.write('|---|---:|---:|---:|---:|\n')
            for row in standings:
                f.write('| {0} | {1} | {2} | {3} | {4} |\n'.format(row['teamName'], row['wins'], row['draws'], row['losses'], row['points']))
            f.close()
