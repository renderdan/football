from unittest import TestCase
from response import Response

testdata = [{u'league': u'BL1', u'numberOfMatchdays': 34, u'lastUpdated': u'2016-03-28T09:10:29Z', u'numberOfGames': 306, u'caption': u'1. Bundesliga 2015/16', u'currentMatchday': 28, u'_links': {u'self': {u'href': u'http://api.football-data.org/v1/soccerseasons/394'}, u'fixtures': {u'href': u'http://api.football-data.org/v1/soccerseasons/394/fixtures'}, u'leagueTable': {u'href': u'http://api.football-data.org/v1/soccerseasons/394/leagueTable'}, u'teams': {u'href': u'http://api.football-data.org/v1/soccerseasons/394/teams'}}, u'year': u'2015', u'numberOfTeams': 18, u'id': 394},
            {u'league': u'PL', u'numberOfMatchdays': 38, u'lastUpdated': u'2016-03-28T09:08:10Z', u'numberOfGames': 380, u'caption': u'Premier League 2015/16', u'currentMatchday': 32, u'_links': {u'self': {u'href': u'http://api.football-data.org/v1/soccerseasons/398'}, u'fixtures': {u'href': u'http://api.football-data.org/v1/soccerseasons/398/fixtures'}, u'leagueTable': {u'href': u'http://api.football-data.org/v1/soccerseasons/398/leagueTable'}, u'teams': {u'href': u'http://api.football-data.org/v1/soccerseasons/398/teams'}}, u'year': u'2015', u'numberOfTeams': 20, u'id': 398},
            {u'league': u'BL2', u'numberOfMatchdays': 34, u'lastUpdated': u'2016-04-02T07:31:02Z', u'numberOfGames': 306, u'caption': u'2. Bundesliga 2015/16', u'currentMatchday': 28, u'_links': {u'self': {u'href': u'http://api.football-data.org/v1/soccerseasons/395'}, u'fixtures': {u'href': u'http://api.football-data.org/v1/soccerseasons/395/fixtures'}, u'leagueTable': {u'href': u'http://api.football-data.org/v1/soccerseasons/395/leagueTable'}, u'teams': {u'href': u'http://api.football-data.org/v1/soccerseasons/395/teams'}}, u'year': u'2015', u'numberOfTeams': 18, u'id': 395}]

expected_links = ['self', 'fixtures', 'leagueTable', 'teams']

class TestResponse(TestCase):
    def test_parse_links(self):
        for idx in range(len(testdata)):
            print idx
            s = Response(testdata[idx])
            links_obj = s.parse_links(testdata[idx]['_links'])
            self.assertFalse(links_obj=={}) # must return a valid object
            self.assertEqual(links_obj,s._response['_links'])
            for link in links_obj:
                self.assertIn(link,expected_links) # fixed set of expected links
                self.assertTrue(links_obj[link]) # cannot have empty string for link url
                print '{0} : {1}'.format(link,links_obj[link])
        pass

