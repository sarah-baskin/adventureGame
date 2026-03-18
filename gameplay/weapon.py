'''
This class dictates the characteristics of weapons
'''

class Weapon:

    def __init__(self, 
                 name : str, 
                 power : int, 
                 defense : int, 
                 sorcery: bool):
        
        self.name = name
        self.power = power
        self.defense = defense
        self.sorcery = sorcery


    def getName():
        return Weapon.name
    
    def getPower():
        return Weapon.power
    
    def getDefense():
        return Weapon.defense
    
    def getSorcery():
        return Weapon.sorcery
    
    def isMagic():
        return True if Weapon.getSorcery() else False