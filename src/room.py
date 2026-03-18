class Room:
    '''
    This class handles the creation of rooms (locations). The places the player can visit
    '''

    def __init__(self,
                 name: str,
                 adjRooms : dict[str, "Room"]):

        self.name = name
        self.adjRooms = adjRooms
    
    def getName(self):
        return self.name
    
    def getAdjacent(self):
        return self.adjRooms
    
    def addAdjacent(self,
                    direc : str,
                    room : "Room"):
        self.adjRooms[direc] = room