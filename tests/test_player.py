import unittest
from src.player import Player, Hand, Satchel
from src.room import Room

class TestPlayer(unittest.TestCase):

    def test_get_name(self):
        player1 = Player("tracy", Room("kitchen", {}, []), 10, Hand([], []), Satchel([]))
        self.assertEqual("tracy", player1.name)

    def test_lose_health(self):
        player1 = Player("tracy", Room("kitchen", {}, []), 10, Hand([], []), Satchel([]))
        player1.lose_health(5)
        self.assertEqual(5, player1.get_health())
    
    def test_gain_health(self):
        player1 = Player("tracy", Room("kitchen", {}, []), 10, Hand([], []), Satchel([]))
        player1.gain_health(5)
        self.assertEqual(15, player1.get_health())
    
    def test_update_loc(self):
        player1 = Player("tracy", Room("kitchen", {}, []), 10, Hand([], []), Satchel([]))
        player1.update_loc(Room("living room", {}, []))
        self.assertEqual("living room", player1.get_location().get_name())

class TestHand(unittest.TestCase):
    
    def test_put_in_left(self):
        ...
    def test_put_in_right(self):
        ...
    def test_take_from_left(self):
        ...
    def test_take_from_right(self):
        ...
    def test_put_in_left_from_right(self):
        ...
    def test_put_in_right_from_left(self):
        ...

class TestSatchel(unittest.TestCase):
    
    def test_put_in_satchel(self):
        ...
    def test_take_out_of_satchel(self):
        ...