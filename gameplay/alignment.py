'''
Alignment chart for charactes to determine personality
'''

from gameplay.skills import Skill

class Alignment:

    name = ""
    description = ""
    skills = []
    weaknesses = []

    def __init__(self, name : str, description : str, skills : list, weaknesses : list):
        self.name = name
        self.description = description
        self.skills = skills
        self.weaknesses = weaknesses
    
    def getName():
        return Alignment.name
    
    def getDescription():
        return Alignment.name
    
    def getSkills():
        return Alignment.skills
    
    def getWeaknesses():
        return Alignment.weaknesses