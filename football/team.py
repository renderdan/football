from response import Response

class Team(Response):
    '''
    This class holds team data for one league
    '''

    def getTeamAttr(self, attr):
        return self._response[attr]