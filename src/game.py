from player import Player, Hand
from item import Item, Satchel
from room import Room

class Game:

    def __init__(self):
        table = Item("Table", "An inconspicuous wooden table", False)
        letter = Item("Letter", "A mysterious letter", True)
        satchel = Satchel("Satchel", "A satchel", True, [])
        spawn = Room("Spawn", {}, {}, [table, letter, satchel])

        self.room_list = [spawn]
        self.player = Player("Sandra Bullock",
                             spawn,
                             10,
                             Hand([], []),
                             None)
    
    def curate_options(self):
        left_rooms = self.player.get_location().get_left()
        right_rooms = self.player.get_location().get_right()
        objects = self.player.get_location().get_objects()

        options = []
        if left_rooms > 0:
            options.append("go left")
            print(f"You have {left_rooms} rooms to explore to your left")
        if right_rooms > 0:
            options.append("go right")
            print(f"You have {right_rooms} rooms to explore to your right")
        if len(objects) > 0:
            options.append("stay here")
            print(f"There are {len(objects)} objects to explore in this room")
        if len(options) == 0:
            print("You are lost forever. Game over.")
        decision = input(f"What do you want to do? You can {", ".join(options)}")
        while not self.verify_decision(decision, options):
            decision = input(f"What do you want to do? You can {", ".join(options)}")
        return decision
    
    def verify_decision(self, decision, options):
        if decision not in options:
            print("Your choice is invalid. Check for a typo.")
            return False
        return True
    
if __name__ == "__main__":
    print("You open your eyes and find yourself in a mysterious room...")
    game = Game()
    decision = game.curate_options()

    
    
