'''
This houses the skill class and its related stuff
'''

# things the player should be able to do:
# have a personality type -- which comes with built in skills and weapons associated with it
# have a satchel -- NEW CLASS NEEDED FOR THIS

from src.room import Room

class Player:
    '''
    Defines player actions and abilities
    '''

    def __init__(self,
                 name : str,
                 location : Room,
                 health : int,
                 gender : str = ""):
        self.name = name
        self.location = location
        self.health = health
        self.gender = gender
    def get_name(self) -> str :
        '''
        Returns the name of a player
        '''
        return self.name
    def get_location(self) -> Room :
        '''
        Returns the current location of a player
        '''
        return self.location
    def get_health(self) -> int :
        '''
        Returns the health level of a player
        An int between 0 -20
        When health is at 0, the player is dead
        '''
        return self.health
    def lose_health(self, num) -> None :
        '''
        The player loses health
        '''
        self.health -= num
    def gain_health(self, num) -> None :
        '''
        The player gains health
        '''
        self.health += num
    def update_loc(self, loc) -> None :
        '''
        Updates the player's current location
        '''
        self.location = loc
    def get_gender(self) -> str :
        '''
        Returns the player's gender
        '''
        return self.gender
