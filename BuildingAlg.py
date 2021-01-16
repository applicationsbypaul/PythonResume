############################################################
## This program will but an algorithm to determine if the
## buildings can be seen at sunset from the west. By 
## default the buildings with 0 are going to be not visible
## thus being gray. When the building can be seen it will 
## be green.
############################################################

class Building:
    def __init__(self, name):
        self.name = name
        self.value = 0
        self.isSeen = False
    def showStat(self):
        print ('-------------')
        print(self.name)
        print(self.value)
        print(self.isSeen)
        print ('-------------')

if __name__ == "__main__":
    a = Building('a')
    b = Building('b')
    c = Building('c')
    d = Building('d')
    e = Building('e')
    buildings = [a,b,c,d,e]
    for value in buildings:
        value.showStat()

