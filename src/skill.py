class Skill:
    '''
    This class handles the creation of player skills

    Advtange is a number between 1 and 5
    Disadvantage is a number between 1 and 5
    '''

    def __init__(self, 
                 name : str, 
                 description : str, 
                 advantage : int, 
                 disadvantage : int):
        self.name = name
        self.description = description
        self.advantage = advantage
        self.disadvantage = disadvantage
    
    def getName(self):
        if not self.name:
            raise ValueError('''To be named is to be known. 
                             This skill must have a name.''')
        return self.name
    
    def getDescription(self):
        if not self.description:
            raise ValueError('''What are words without definitions? 
                             This skill must have a description''')
        return self.description
    
    def getAdvantage(self):
        return self.advantage
    
    def getDisadvantage(self):
        return self.disadvantage