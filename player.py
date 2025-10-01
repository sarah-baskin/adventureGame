import sys
from weapon import Weapon

'''
This class will contain all of the information necessary for creating a player in the game
'''

class Player:

    name = "Player 1"
    skills = []
    weapons = []
    currWeapon = None
    personality = "True Neutral"
    position = "Game Start"
    

    def __init__(self):
        pass
    
    def __init__(self, name : str, skills : list, weapons : list, personality : str):
        self.name = name
        self.skills = skills
        self.weapons = weapons
        self.personality = personality

    def sayName():
        return Player.name
    
    def showWeapons():
        if len(Player.weapons) == 0:
            print("You are defenseless.")
        elif len(Player.weapons) == 1 and Player.weapons[0] == Player.currWeapon:
            print("You are already armed with your only weapon")
        else:
            print("Here is what you have in your arsenal: ")
            for weapon in Player.weapons:
                if weapon != Player.currWeapon:
                    print(weapon.getName())
    
    def pickWeapon():
        if len(Player.weapons) == 0:
            print("You are defenseless.")
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
    
    def addWeapon(weapon : Weapon):
        Player.weapons.add(weapon)
                

    
