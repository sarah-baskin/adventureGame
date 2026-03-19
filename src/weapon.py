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
                 sorcery: bool,
                 label : str = None):
        
        self.name = name
        self.power = power
        self.defense = defense
        self.sorcery = sorcery
        self.label = label

    def getName(self) -> str :
        return self.name
    
    def getPower(self) -> int :
        return self.power
    
    def getDefense(self) -> int :
        return self.defense
    
    def getSorcery(self) -> bool :
        return self.sorcery
    
    def isMagic(self) -> bool:
        return True if self.getSorcery() else False

    def getLabel(self) -> str:
        return self.label