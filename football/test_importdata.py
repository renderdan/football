from unittest import TestCase
from importdata import Import

class TestImportData(TestCase):
    def test_importdata_constructs(self):
        i = Import()
        self.assertIsInstance(i, Import)
        pass

    def test_importdata_importurlfromrest(self):
        i = Import()
        results = i.importurlfromrest('http://api.football-data.org/v1/soccerseasons/?season=2015')
        self.assertIsNotNone(results)
        self.assertGreater(len(results),0)
        for result in results:
            assert(result)
            print result
        pass
