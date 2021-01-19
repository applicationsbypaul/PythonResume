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
        buildingsList = BuildingAlg.createBuildings()
        BuildingAlg.changeBuilding(1, 2, self.buildingsList)
        self.assertEqual(self.buildingsList[1].value, 2)

    def test_CreateBuildings(self):
        #buildingsList = BuildingAlg.createBuildings()
        self.assertGreater(len(self.buildingsList), 0)

    def test_alg(self):
        BuildingAlg.changeBuilding(1,2, self.buildingsList)
        self.assertEqual(self.buildingsList[0].isSeen, False)
        self.assertEqual(self.buildingsList[1].isSeen, True)
        self.assertEqual(self.buildingsList[2].isSeen, False)
        self.assertEqual(self.buildingsList[3].isSeen, False)
        self.assertEqual(self.buildingsList[4].isSeen, False)
    def test_alg_mutipleChanges(self):
        BuildingAlg.changeBuilding(1,2, self.buildingsList)
        BuildingAlg.changeBuilding(4,7, self.buildingsList)
        BuildingAlg.changeBuilding(2,4, self.buildingsList)
        self.assertEqual(self.buildingsList[0].isSeen, False)
        self.assertEqual(self.buildingsList[1].isSeen, True)
        self.assertEqual(self.buildingsList[2].isSeen, True)
        self.assertEqual(self.buildingsList[3].isSeen, False)
        self.assertEqual(self.buildingsList[4].isSeen, True)
    
    def test_alg_mutipleChanges2(self):
        BuildingAlg.changeBuilding(1,2, self.buildingsList)
        BuildingAlg.changeBuilding(4,7, self.buildingsList)
        BuildingAlg.changeBuilding(2,1, self.buildingsList)
        self.assertEqual(self.buildingsList[0].isSeen, False)
        self.assertEqual(self.buildingsList[1].isSeen, True)
        self.assertEqual(self.buildingsList[2].isSeen, False)
        self.assertEqual(self.buildingsList[3].isSeen, False)
        self.assertEqual(self.buildingsList[4].isSeen, True)


if __name__ == "__main__":
    unittest.main()
