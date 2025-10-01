from weapon.py import Weapon

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
    
    def __init__(self, name, skills, weapons, personality):
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
                    print(weapon)
    
    def pickWeapon():
        if len(Player.weapons) == 0:
            print("You are defenseless.")
        elif len(Player.weapons) == 1 and Player.weapons[0] == Player.currWeapon:
            print("You are already armed with your only weapon")
        else:
            Player.showWeapons()
            choice = input("What weapon do you want to select? ")

    
