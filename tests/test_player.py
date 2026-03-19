import unittest
from src.player import Player
from src.room import Room

class TestPlayer(unittest.TestCase):

    def test_get_name(self):
        player1 = Player("tracy", Room("kitchen", {}), 10, None)
        self.assertEqual("tracy", player1.name)

    def test_lose_health(self):
        player1 = Player("tracy", Room("kitchen", {}), 10, None)
        player1.loseHealth(5)
        self.assertEqual(5, player1.getHealth())
    
    def test_gain_health(self):
        player1 = Player("tracy", Room("kitchen", {}), 10, None)
        player1.gainHealth(5)
        self.assertEqual(15, player1.getHealth())
    
    def test_update_loc(self):
        player1 = Player("tracy", Room("kitchen", {}), 10, None)
        player1.updateLoc(Room("living room", {}))
        self.assertEqual("living room", player1.getLocation().getName())
    
    def test_create_player_with_gender(self):
        player1 = Player("tracy", Room("kitchen", {}), 10, "female")
        self.assertEqual("female", player1.getGender())