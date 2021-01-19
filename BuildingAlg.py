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
    #step one interate through from the end to the start.
    highestBuilding = 0
    for index in range(len(buildingList)):
        ## first check the first value we will see if it is greater than 0 
        # making it seen first
        # i need a marker for biggest value
        if index == 0:
            if buildingList[index].value == 0:
                buildingList[index].isSeen = False
                continue
            else:
                buildingList[index].isSeen = True
                highestBuilding = buildingList[index].value
                continue
        #checking now to see anything after the first index
        # confirm that its bigger than 0 if not make it not seen
        if buildingList[index].value > 0:
            #gather data to compare easier
            current = buildingList[index].value
            previous = buildingList[index - 1].value
            if current > previous and current > highestBuilding:
                buildingList[index].isSeen = True
                highestBuiling = buildingList[index].value
            else:
                buildingList[index].isSeen = False
        else:
            buildingList[index].isSeen = False

def changeBuilding(building, value, buildingList):
    """
    Changes the building height of
    a building. building will be an int
    """
    buildingList[building].value = value
    buildingAlg(buildingList)


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
   pass


    
