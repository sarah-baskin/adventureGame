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
                 gender : str = None):
        
        self.name = name
        self.location = location
        self.health = health
        self.gender = gender
    
    def getName(self):
        return self.name
    
    def getLocation(self):
        return self.location
    
    def getHealth(self):
        return self.health
    
    def loseHealth(self, num):
        self.health -= num
    
    def gainHealth(self, num):
        self.health += num

    def updateLoc(self, loc):
        self.location = loc
    
    def getGender(self):
        return self.gender