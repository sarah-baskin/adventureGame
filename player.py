import sys
from weapon import Weapon
from skills import Skill
from alignment import Alignment
from room import Room

'''
This class will contain all of the information necessary for creating a player in the game
'''

class Player:

    name = "Jane Doe"
    skills = []
    weapons = []
    currWeapon = None
    alignment = None
    position = None
    

    def __init__(self):
        pass

    
    def __init__(self, name : str, skills : list, weapons : list, alignment : Alignment, position : Room):
        self.name = name
        self.skills = skills
        self.weapons = weapons
        self.personality = alignment
        self.position = position

    def getName():
        return Player.name
    
    def showWeapons():
        if len(Player.weapons) == 0:
            print("You are defenseless. Use your fists.")
        elif len(Player.weapons) == 1 and Player.weapons[0] == Player.currWeapon:
            print("You are already armed with your only weapon")
        else:
            print("Here is what you have in your arsenal: ")
            for weapon in Player.weapons:
                if weapon != Player.currWeapon:
                    print(weapon.getName())
    
    def pickWeapon():
        if len(Player.weapons) == 0:
            print("You are defenseless. Use your fists.")
        elif len(Player.weapons) == 1 and Player.weapons[0] == Player.currWeapon:
            print("You are already armed with your only weapon")
        else:
            Player.showWeapons()
            prevCurr = Player.currWeapon
            choice = input("What weapon do you want to select? ")
            while prevCurr == Player.currWeapon:
                for weapon in Player.weapons:
                    if choice == weapon.getName():
                        Player.currWeapon = weapon
                if Player.currWeapon == prevCurr:
                    print("The weapon that you desire is not in your arsenal.")
                    Player.showWeapons()
    
    def addWeaponToWeapons(weapon : Weapon):
        Player.weapons.add(weapon)

    def showSkills():
        if len(Player.skills) == 0:
            print("You have yet to collect your first skill.")
        else:
            print("Here are your skills: ")
            for skill in Player.skills:
                print(skill.getName())

    def addSkillToSkills(skill : Skill):
        Player.skills.add(skill)
                

    
