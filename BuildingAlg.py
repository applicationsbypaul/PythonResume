############################################################
# This program will but an algorithm to determine if the
# buildings can be seen at sunset from the west. By
# default the buildings with 0 are going to be not visible
# thus being gray. When the building can be seen it will
# be green.
############################################################

class Building:
    def __init__(self, name):
        self.name = name
        self.value = 0
        self.isSeen = False

    def __str__(self):
        response = f'------------\n'\
            'Building Name = {}\n'\
            'Building Value = {}\n'\
            'Building isSeen = {}\n'\
            '------------'\
            .format(self.name, self.value, self.isSeen)
        return response


def buildingAlg(buildingList):
    """
    The algorith to see if 
    the sun can see the buildings
    """
    print(len(buildingsList))

def changeBuilding(building, value, buildingList):
    """
    Changes the building height of
    a building. building will be an int
    """
    buildingList[building].value = value


def createBuildings():
    """
    generates a sample of buildings
    """
    a = Building('a')
    b = Building('b')
    c = Building('c')
    d = Building('d')
    e = Building('e')
    buildings = [a, b, c, d, e]
    return buildings


if __name__ == "__main__":
    buildingsList = createBuildings()
    for building in buildingsList:
        print(building)
    changeBuilding(1,1,buildingsList)
    for building in buildingsList:
        print(building)
