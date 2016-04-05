from unittest import TestCase
from importseasons import ImportSeasons

class TestImportseasons(TestCase):
    def test_importseasons_constructs(self):
        i = ImportSeasons()
        self.assertIsInstance(i, ImportSeasons)
        self.assertEqual(i.seasons_list,[])
        pass

    def test_importseasons_importurlfromrest(self):
        i = ImportSeasons()
        results = i.importurlfromrest('http://api.football-data.org/v1/soccerseasons/?season=2015')
        self.assertIsNotNone(results)
        self.assertGreater(len(results),0)
        for result in results:
            assert(result)
            print result
        pass
