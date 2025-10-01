'''
This class dictates the characteristics of weapons
'''

class Weapon:

    name = ""
    power = 0
    defense = 0
    sorcery = 0

    def __init__(self, name, power, defense, sorcery):
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
        return True if Weapon.sorcery > 0 else False