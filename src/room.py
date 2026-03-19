'''
This houses the skill class and its related stuff
'''

class Room:
    '''
    This class handles the creation of rooms (locations). The places the player can visit
    '''

    def __init__(self,
                 name: str,
                 adj_rooms : dict[str, list["Room"]]):
        self.name = name
        self.adj_rooms = adj_rooms
    def get_name(self) -> str :
        '''
        Returns the room's name
        '''
        return self.name
    def get_adjacent(self) -> dict[str, list["Room"]] :
        '''
        Returns the dictionary of adjacent rooms associated with this room
        '''
        return self.adj_rooms
    def add_adjacent(self,
                    direc : str,
                    room : "Room"):
        '''
        Adds a room to the adjacent room list
        '''

        if direc not in self.adj_rooms:
            self.adj_rooms[direc] = [room]
        else:
            self.adj_rooms[direc].append(room)
