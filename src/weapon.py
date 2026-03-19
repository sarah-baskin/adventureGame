'''
This houses the skill class and its related stuff
'''

class Weapon:
    '''
    This class dictates the characteristics of weapons

    Power can be zero, max can be 10
    Defense can be zero, max can be 10
    '''

    def __init__(self,
                 name : str,
                 power : int,
                 defense : int,
                 sorcery: bool
                 ):
        self.name = name
        self.power = power
        self.defense = defense
        self.sorcery = sorcery

    def get_name(self) -> str :
        '''
        Returns the weapon's name
        '''
        return self.name
    def get_power(self) -> int :
        '''
        Returns the power ability of the weapon
        An int 0-5
        '''
        return self.power
    def get_defense(self) -> int :
        '''
        Returns the defensive ability of the weapon
        An int 0-5
        '''
        return self.defense
    def get_sorcery(self) -> bool :
        '''
        Returns whether the weapon is imbued with magic
        '''
        return self.sorcery
