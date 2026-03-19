import unittest
from src.room import Room
from src.item import Item

class TestRoom(unittest.TestCase):

    def test_get_name(self):
        kitchen = Room("kitchen", {}, [])
        self.assertEqual("kitchen", kitchen.get_name())
    
    def test_get_empty_adj(self):
        kitchen = Room("kitchen", {}, [])
        self.assertFalse(kitchen.get_adjacent())
    
    def test_get_full_adj(self):
        kitchen = Room("kitchen", {"l": [Room("dining room", {}, [])], "r": [Room("parlor", {}, [])]}, [])
        left_rooms = kitchen.get_adjacent()["l"]
        self.assertEqual(1, len(left_rooms))

        right_rooms = kitchen.get_adjacent()["r"]
        self.assertEqual(1, len(right_rooms))
    
    def test_add_adj_to_empty(self):
        kitchen = Room("kitchen", {}, [])
        kitchen.add_adjacent("l", Room("bathroom", {}, []))
        left_rooms = kitchen.get_adjacent()["l"]
        self.assertEqual(1, len(left_rooms))

    def test_add_adj_to_created_dict(self):
        kitchen = Room("kitchen", {"l": [Room("dining room", {}, [])], "r": [Room("parlor", {}, [])]}, [])
        kitchen.add_adjacent("l", Room("bathroom", {}, []))
        left_rooms = kitchen.get_adjacent()["l"]
        self.assertEqual(2, len(left_rooms))
    
    def test_add_r_room_to_created_dict(self):
        kitchen = Room("kitchen", {"l": [Room("dining room", {}, [])]}, [])
        kitchen.add_adjacent("r", Room("parlor", {}, []))
        right_rooms = kitchen.get_adjacent()["r"]
        self.assertEqual(1, len(right_rooms))
    
    def test_get_object_from_room(self):
        kitchen = Room("kitchen", {}, [Item("letter", "pen on paper")])
        self.assertEqual(1, len(kitchen.get_objects()))
        self.assertEqual("letter", kitchen.get_objects()[0].get_name())
    
    def test_add_object_to_room(self):
        kitchen = Room("kitchen", {}, [])
        self.assertEqual(0, len(kitchen.get_objects()))

        new_item_1 = Item("letter", "pen on paper")
        kitchen.add_object(new_item_1)
        self.assertEqual(1, len(kitchen.get_objects()))
        self.assertEqual("letter", kitchen.get_objects()[0].get_name())

        new_item_2 = Item("Bag", "just a normal paper bag")
        kitchen.add_object(new_item_2)
        self.assertEqual(2, len(kitchen.get_objects()))
        self.assertEqual("Bag", kitchen.get_objects()[1].get_name())