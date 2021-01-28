/**
 * Constructing this in javascript just to implement in my website
 */
class Building {
    constructor(name) {
        this.name = name;
        this.value = 0;
        this.isSeen = false;
    }
};

 var buildings = [];
/**
 * This function will create the buildings and put them
 * in an array to be examined.
 */
function createBuildings() {
    buildings = [];
    let buildingA = new Building("A");
    let buildingB = new Building("B");
    let buildingC = new Building("C");
    let buildingD = new Building("D");
    let buildingE = new Building("E");

   buildings.push(buildingA,buildingB,
    buildingC,buildingD,buildingE)
    buildingAlg()
}

function buildingAlg() {
    let highestBuilding = 0;
    for (let index = 0; index < buildings.length; index++) {
        if (index == 0){
            if (buildings[index].value == 0){
                buildings[index].isSeen = false;
                continue;
            }
            else{
                buildings[index].isSeen = true;
                highestBuilding = buildings[index].value;
            }
        }
        
    }
}

