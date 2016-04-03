from response import Response

class Season(Response):
    '''
    This class holds season data for one league
    '''

    def getLeague(self):
        return self._response['league']

    def isLeague(self, league):
        return self._response['caption'].startswith(league)

    def getLinksUrl(self, link):
        links_obj = self._response['_links']
        return links_obj[link]