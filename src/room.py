'''
This houses the skill class and its related stuff
'''
from item import Item

class Room:
    '''
    This class handles the creation of rooms (locations). The places the player can visit
    '''

    def __init__(self,
                 name: str,
                 adj_rooms : dict[str, list["Room"]],
                 known_adj_rooms : dict[str, list["Room"]],
                 objects : list[Item]):
        self.name = name
        self.adj_rooms = adj_rooms
        self.known_adj_rooms = known_adj_rooms
        self.objects = objects
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
    def get_known_adjacent(self) -> dict[str, list["Room"]]:
        return self.known_adj_rooms
    def get_left(self) -> int:
        return self.adj_rooms["l"] if self.adj_rooms and self.adj_rooms["l"] else 0
    def get_right(self) -> int:
        return self.adj_rooms["r"] if self.adj_rooms and self.adj_rooms["r"] else 0
    def get_objects(self) -> list[Item]:
        return self.objects
    def add_adjacent(self,
                    direc : str,
                    room : "Room"):
        '''
        Adds a room to the the known adjacent room list
        '''
        if direc not in self.known_adj_rooms:
            self.known_adj_rooms[direc] = [room]
        else:
            self.known_adj_rooms[direc].append(room)
    def add_object(self, 
                   object : Item) -> None:
        '''
        Add an object to the list of available items in the room
        '''
        self.objects.append(object)
