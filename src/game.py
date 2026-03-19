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
        print("Possible actions: ")
        if left_rooms > 0:
            options.append("go left")
            print("- Explore the room to your left")
        if right_rooms > 0:
            options.append("go right")
            print("- Explore the room to your right")
        if len(objects) > 0:
            options.append("stay here")
            print("- Check out what there is to see here.")
        
        if len(options) == 0:
            print("You are lost forever. Game over.")
            decision = None
        elif len(options) == 1:
            print(f"Your only option is to {options[0]}. Let's do that.")
            decision = options[0]
        elif len(options) > 1:
            print(f"What do you want to do? Your options are: {", ".join(options)}")
            decision = input("Pick an action from the choices above: ")
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

    
    
