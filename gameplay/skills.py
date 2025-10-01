'''
This class handles the creation of player skills
'''

class Skill:

    name = ""
    description = ""
    advantage = 0
    disadvantage = 0

    def __init__(self, name : str, description : str, advantage : int, disadvantage : int):
        self.name = name
        self.description = description
        self.advantage = advantage
        self.disadvantage = disadvantage
    
    def getName():
        return Skill.name
    
    def getDescription():
        return Skill.description
    
    def getAdvantage():
        return Skill.advantage
    
    def getDisadvantage():
        return Skill.disadvantage