from unittest import TestCase
from season import Season

testdata = [{u'league': u'BL1', u'numberOfMatchdays': 34, u'lastUpdated': u'2016-03-28T09:10:29Z', u'numberOfGames': 306, u'caption': u'1. Bundesliga 2015/16', u'currentMatchday': 28, u'_links': {u'self': {u'href': u'http://api.football-data.org/v1/soccerseasons/394'}, u'fixtures': {u'href': u'http://api.football-data.org/v1/soccerseasons/394/fixtures'}, u'leagueTable': {u'href': u'http://api.football-data.org/v1/soccerseasons/394/leagueTable'}, u'teams': {u'href': u'http://api.football-data.org/v1/soccerseasons/394/teams'}}, u'year': u'2015', u'numberOfTeams': 18, u'id': 394},
            {u'league': u'BL2', u'numberOfMatchdays': 34, u'lastUpdated': u'2016-04-02T07:31:02Z', u'numberOfGames': 306, u'caption': u'2. Bundesliga 2015/16', u'currentMatchday': 28, u'_links': {u'self': {u'href': u'http://api.football-data.org/v1/soccerseasons/395'}, u'fixtures': {u'href': u'http://api.football-data.org/v1/soccerseasons/395/fixtures'}, u'leagueTable': {u'href': u'http://api.football-data.org/v1/soccerseasons/395/leagueTable'}, u'teams': {u'href': u'http://api.football-data.org/v1/soccerseasons/395/teams'}}, u'year': u'2015', u'numberOfTeams': 18, u'id': 395},
            {u'league': u'FL1', u'numberOfMatchdays': 38, u'lastUpdated': u'2016-03-23T11:00:02Z', u'numberOfGames': 380, u'caption': u'Ligue 1 2015/16', u'currentMatchday': 32, u'_links': {u'self': {u'href': u'http://api.football-data.org/v1/soccerseasons/396'}, u'fixtures': {u'href': u'http://api.football-data.org/v1/soccerseasons/396/fixtures'}, u'leagueTable': {u'href': u'http://api.football-data.org/v1/soccerseasons/396/leagueTable'}, u'teams': {u'href': u'http://api.football-data.org/v1/soccerseasons/396/teams'}}, u'year': u'2015', u'numberOfTeams': 20, u'id': 396},
            {u'league': u'FL2', u'numberOfMatchdays': 38, u'lastUpdated': u'2016-03-24T11:00:03Z', u'numberOfGames': 380, u'caption': u'Ligue 2 2015/16', u'currentMatchday': 32, u'_links': {u'self': {u'href': u'http://api.football-data.org/v1/soccerseasons/397'}, u'fixtures': {u'href': u'http://api.football-data.org/v1/soccerseasons/397/fixtures'}, u'leagueTable': {u'href': u'http://api.football-data.org/v1/soccerseasons/397/leagueTable'}, u'teams': {u'href': u'http://api.football-data.org/v1/soccerseasons/397/teams'}}, u'year': u'2015', u'numberOfTeams': 20, u'id': 397},
            {u'league': u'PL', u'numberOfMatchdays': 38, u'lastUpdated': u'2016-03-28T09:08:10Z', u'numberOfGames': 380, u'caption': u'Premier League 2015/16', u'currentMatchday': 32, u'_links': {u'self': {u'href': u'http://api.football-data.org/v1/soccerseasons/398'}, u'fixtures': {u'href': u'http://api.football-data.org/v1/soccerseasons/398/fixtures'}, u'leagueTable': {u'href': u'http://api.football-data.org/v1/soccerseasons/398/leagueTable'}, u'teams': {u'href': u'http://api.football-data.org/v1/soccerseasons/398/teams'}}, u'year': u'2015', u'numberOfTeams': 20, u'id': 398},
            {u'league': u'PD', u'numberOfMatchdays': 38, u'lastUpdated': u'2016-03-28T09:03:30Z', u'numberOfGames': 380, u'caption': u'Primera Division 2015/16', u'currentMatchday': 31, u'_links': {u'self': {u'href': u'http://api.football-data.org/v1/soccerseasons/399'}, u'fixtures': {u'href': u'http://api.football-data.org/v1/soccerseasons/399/fixtures'}, u'leagueTable': {u'href': u'http://api.football-data.org/v1/soccerseasons/399/leagueTable'}, u'teams': {u'href': u'http://api.football-data.org/v1/soccerseasons/399/teams'}}, u'year': u'2015', u'numberOfTeams': 20, u'id': 399},
            {u'league': u'SD', u'numberOfMatchdays': 42, u'lastUpdated': u'2016-03-30T04:00:06Z', u'numberOfGames': 462, u'caption': u'Segunda Division 2015/16', u'currentMatchday': 32, u'_links': {u'self': {u'href': u'http://api.football-data.org/v1/soccerseasons/400'}, u'fixtures': {u'href': u'http://api.football-data.org/v1/soccerseasons/400/fixtures'}, u'leagueTable': {u'href': u'http://api.football-data.org/v1/soccerseasons/400/leagueTable'}, u'teams': {u'href': u'http://api.football-data.org/v1/soccerseasons/400/teams'}}, u'year': u'2015', u'numberOfTeams': 22, u'id': 400},
            {u'league': u'SA', u'numberOfMatchdays': 38, u'lastUpdated': u'2016-03-30T21:25:20Z', u'numberOfGames': 380, u'caption': u'Serie A 2015/16', u'currentMatchday': 31, u'_links': {u'self': {u'href': u'http://api.football-data.org/v1/soccerseasons/401'}, u'fixtures': {u'href': u'http://api.football-data.org/v1/soccerseasons/401/fixtures'}, u'leagueTable': {u'href': u'http://api.football-data.org/v1/soccerseasons/401/leagueTable'}, u'teams': {u'href': u'http://api.football-data.org/v1/soccerseasons/401/teams'}}, u'year': u'2015', u'numberOfTeams': 20, u'id': 401},
            {u'league': u'PPL', u'numberOfMatchdays': 34, u'lastUpdated': u'2016-03-28T09:05:38Z', u'numberOfGames': 306, u'caption': u'Primeira Liga 2015/16', u'currentMatchday': 28, u'_links': {u'self': {u'href': u'http://api.football-data.org/v1/soccerseasons/402'}, u'fixtures': {u'href': u'http://api.football-data.org/v1/soccerseasons/402/fixtures'}, u'leagueTable': {u'href': u'http://api.football-data.org/v1/soccerseasons/402/leagueTable'}, u'teams': {u'href': u'http://api.football-data.org/v1/soccerseasons/402/teams'}}, u'year': u'2015', u'numberOfTeams': 18, u'id': 402},
            {u'league': u'BL3', u'numberOfMatchdays': 38, u'lastUpdated': u'2016-03-28T09:12:05Z', u'numberOfGames': 380, u'caption': u'3. Bundesliga 2015/16', u'currentMatchday': 32, u'_links': {u'self': {u'href': u'http://api.football-data.org/v1/soccerseasons/403'}, u'fixtures': {u'href': u'http://api.football-data.org/v1/soccerseasons/403/fixtures'}, u'leagueTable': {u'href': u'http://api.football-data.org/v1/soccerseasons/403/leagueTable'}, u'teams': {u'href': u'http://api.football-data.org/v1/soccerseasons/403/teams'}}, u'year': u'2015', u'numberOfTeams': 20, u'id': 403},
            {u'league': u'DED', u'numberOfMatchdays': 34, u'lastUpdated': u'2016-03-23T05:00:10Z', u'numberOfGames': 306, u'caption': u'Eredivisie 2015/16', u'currentMatchday': 29, u'_links': {u'self': {u'href': u'http://api.football-data.org/v1/soccerseasons/404'}, u'fixtures': {u'href': u'http://api.football-data.org/v1/soccerseasons/404/fixtures'}, u'leagueTable': {u'href': u'http://api.football-data.org/v1/soccerseasons/404/leagueTable'}, u'teams': {u'href': u'http://api.football-data.org/v1/soccerseasons/404/teams'}}, u'year': u'2015', u'numberOfTeams': 18, u'id': 404},
            {u'league': u'CL', u'numberOfMatchdays': 10, u'lastUpdated': u'2016-03-31T13:42:06Z', u'numberOfGames': 120, u'caption': u'Champions League 2015/16', u'currentMatchday': 8, u'_links': {u'self': {u'href': u'http://api.football-data.org/v1/soccerseasons/405'}, u'fixtures': {u'href': u'http://api.football-data.org/v1/soccerseasons/405/fixtures'}, u'leagueTable': {u'href': u'http://api.football-data.org/v1/soccerseasons/405/leagueTable'}, u'teams': {u'href': u'http://api.football-data.org/v1/soccerseasons/405/teams'}}, u'year': u'2015', u'numberOfTeams': 32, u'id': 405},
            {u'league': u'EL1', u'numberOfMatchdays': 46, u'lastUpdated': u'2016-04-01T04:00:12Z', u'numberOfGames': 552, u'caption': u'League One 2015/16', u'currentMatchday': 40, u'_links': {u'self': {u'href': u'http://api.football-data.org/v1/soccerseasons/425'}, u'fixtures': {u'href': u'http://api.football-data.org/v1/soccerseasons/425/fixtures'}, u'leagueTable': {u'href': u'http://api.football-data.org/v1/soccerseasons/425/leagueTable'}, u'teams': {u'href': u'http://api.football-data.org/v1/soccerseasons/425/teams'}}, u'year': u'2015', u'numberOfTeams': 24, u'id': 425}]

expected_links = ['self', 'fixtures', 'leagueTable', 'teams']

class TestSeason(TestCase):
    def test_season_can_construct(self):
        for i in range(len(testdata)):
            s = Season(testdata[i])
            self.assertIsInstance(s, Season)
            print i, s
        pass

    def test_parse_links(self):
        s = Season(testdata[0])
        links_obj = s.parse_links(testdata[0]['_links'])
        self.assertFalse(links_obj=={}) # must return a valid object
        self.assertEqual(links_obj,s._response['_links'])
        for link in links_obj:
            self.assertIn(link,expected_links) # fixed set of expected links
            self.assertTrue(links_obj[link]) # cannot have empty string for link url
            print '{0} : {1}'.format(link,links_obj[link])
        pass

    def test_is_premier_league(self):
        s = Season(testdata[4])
        self.assertTrue(s.isLeague('Premier League'))
        self.assertEqual(s.getLeague(),'PL')
        print 'getLeague returned : ',s.getLeague()
        pass

    def test_teams_url(self):
        s = Season(testdata[4])
        url = s.getLinksUrl('teams')
        self.assertEqual(url,'http://api.football-data.org/v1/soccerseasons/398/teams')
        pass
