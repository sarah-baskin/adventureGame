'''
This houses the skill class and its related stuff
'''

# things the player should be able to do:
# have a personality type -- which comes with built in skills and weapons associated with it
# have a satchel -- NEW CLASS NEEDED FOR THIS

from room import Room
from item import Item, Satchel

class Hand:
    '''
    Defines evrything held in a player's hand at any given time
    '''
    def __init__(self,
                 left_hand : list[Item],
                 right_hand : list[Item]):
        self.left_hand = left_hand
        self.right_hand = right_hand
    def get_left_hand(self) -> list[Item]:
        return self.left_hand
    def get_right_hand(self) -> list[Item]:
        return self.right_hand
    def add_to_left_hand(self,
                         obj : Item) -> None:
        self.left_hand.append(obj)
    def add_to_right_hand(self,
                          obj : Item) -> None:
        self.right_hand.append(obj)
    def del_from_left_hand(self,
                         obj : Item) -> None:
        self.left_hand.remove(obj)
    def del_from_right_hand(self,
                          obj : Item) -> None:
        self.right_hand.remove(obj)

class Player:
    '''
    Defines player actions and abilities
    '''

    def __init__(self,
                 name : str,
                 location : Room,
                 health : int,
                 hand : Hand,
                 satchel : Satchel):
        self.name = name
        self.location = location
        self.health = health
        self.hand = hand
        self.satchel = satchel
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
    
