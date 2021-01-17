import BuildingAlg
import unittest

buildingsList = []


class Test_TestBuildingAlg(unittest.TestCase):

    def setUp(self):
        self.buildingsList = BuildingAlg.createBuildings()

    def tearDown(self):
        del self.buildingsList

    def test_ChangeBuilding(self):
        """
        Testing to confirm I can the building values
        """
        #buildingsList = BuildingAlg.createBuildings()
        BuildingAlg.changeBuilding(1, 2, self.buildingsList)
        newvalue = self.buildingsList[1].value
        self.assertEqual(self.buildingsList[1].value, 2)

    def test_CreateBuildings(self):
        #buildingsList = BuildingAlg.createBuildings()
        self.assertGreater(len(self.buildingsList), 0)


if __name__ == "__main__":
    unittest.main()
