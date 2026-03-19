import unittest
from src.player import Player, Hand, Satchel
from src.room import Room
from src.item import Item

class TestPlayer(unittest.TestCase):

    def test_get_name(self):
        player1 = Player("tracy", Room("kitchen", {}, {}, []), 10, Hand([], []), Satchel([]))
        self.assertEqual("tracy", player1.name)

    def test_lose_health(self):
        player1 = Player("tracy", Room("kitchen", {}, {}, []), 10, Hand([], []), Satchel([]))
        player1.lose_health(5)
        self.assertEqual(5, player1.get_health())
    
    def test_gain_health(self):
        player1 = Player("tracy", Room("kitchen", {}, {}, []), 10, Hand([], []), Satchel([]))
        player1.gain_health(5)
        self.assertEqual(15, player1.get_health())
    
    def test_update_loc(self):
        player1 = Player("tracy", Room("kitchen", {}, {}, []), 10, Hand([], []), Satchel([]))
        player1.update_loc(Room("living room", {}, {}, []))
        self.assertEqual("living room", player1.get_location().get_name())

class TestHand(unittest.TestCase):
    
    def test_put_in_left(self):
        my_hand = Hand([], [])
        obj = Item("letter", "pen and paper")
        my_hand.add_to_left_hand(obj)
        self.assertEqual(1, len(my_hand.get_left_hand()))
        self.assertEqual("letter", my_hand.get_left_hand()[0].get_name())

    def test_put_in_right(self):
        my_hand = Hand([], [])
        obj = Item("letter", "pen and paper")
        my_hand.add_to_right_hand(obj)
        self.assertEqual(1, len(my_hand.get_right_hand()))
        self.assertEqual("letter", my_hand.get_right_hand()[0].get_name())

    def test_take_from_left(self):
        letter = Item("letter", "pen and paper")
        my_hand = Hand([letter], [])
        my_hand.del_from_left_hand(letter)
        self.assertEqual(0, len(my_hand.get_left_hand()))

    def test_take_from_right(self):
        letter = Item("letter", "pen and paper")
        my_hand = Hand([], [letter])
        my_hand.del_from_right_hand(letter)
        self.assertEqual(0, len(my_hand.get_right_hand()))

    def test_put_in_left_from_right(self):
        letter = Item("letter", "pen and paper")
        my_hand = Hand([], [letter])
        my_hand.del_from_right_hand(letter)
        my_hand.add_to_left_hand(letter)
        self.assertEqual(1, len(my_hand.get_left_hand()))
        self.assertEqual(0, len(my_hand.get_right_hand()))

    def test_put_in_right_from_left(self):
        letter = Item("letter", "pen and paper")
        my_hand = Hand([letter], [])
        my_hand.del_from_left_hand(letter)
        my_hand.add_to_right_hand(letter)
        self.assertEqual(0, len(my_hand.get_left_hand()))
        self.assertEqual(1, len(my_hand.get_right_hand()))

class TestSatchel(unittest.TestCase):
    
    def test_put_in_satchel(self):
        letter = Item("letter", "pen and paper")
        my_satchel = Satchel([])
        my_satchel.add_to_holding(letter)
        self.assertEqual(1, len(my_satchel.get_holding()))
        self.assertEqual("letter", my_satchel.get_holding()[0].get_name())

    def test_take_out_of_satchel(self):
        letter = Item("letter", "pen and paper")
        my_satchel = Satchel([letter])
        self.assertEqual(1, len(my_satchel.get_holding()))
        my_satchel.remove_from_holding(letter)
        self.assertEqual(0, len(my_satchel.get_holding()))
