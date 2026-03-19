import unittest
from src.room import Room

class TestRoom(unittest.TestCase):

    def test_get_name(self):
        kitchen = Room("kitchen", {})
        self.assertEqual("kitchen", kitchen.getName())
    
    def test_get_empty_adj(self):
        kitchen = Room("kitchen", {})
        self.assertFalse(kitchen.getAdjacent())
    
    def test_get_full_adj(self):
        kitchen = Room("kitchen", {"l": [Room("dining room", {})], "r": [Room("parlor", {})]})
        left_rooms = kitchen.getAdjacent()["l"]
        self.assertEqual(1, len(left_rooms))

        right_rooms = kitchen.getAdjacent()["r"]
        self.assertEqual(1, len(right_rooms))
    
    def test_add_adj_to_empty(self):
        kitchen = Room("kitchen", {})
        kitchen.addAdjacent("l", Room("bathroom", {}))
        left_rooms = kitchen.getAdjacent()["l"]
        self.assertEqual(1, len(left_rooms))

    def test_add_adj_to_created_dict(self):
        kitchen = Room("kitchen", {"l": [Room("dining room", {})], "r": [Room("parlor", {})]})
        kitchen.addAdjacent("l", Room("bathroom", {}))
        left_rooms = kitchen.getAdjacent()["l"]
        self.assertEqual(2, len(left_rooms))
    
    def test_add_r_room_to_created_dict(self):
        kitchen = Room("kitchen", {"l": [Room("dining room", {})]})
        kitchen.addAdjacent("r", Room("parlor", {}))
        right_rooms = kitchen.getAdjacent()["r"]
        self.assertEqual(1, len(right_rooms))