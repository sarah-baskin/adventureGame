import unittest
from weapon import Weapon

class TestWeapon(unittest.TestCase):

    def swordTest():
        sword = Weapon("sword", 4, 3, 0)
        self.assertEqual("sword", sword.getName())
        self.assertEqual(False, sword.isMagic())
    
    def hammerTest():
        hammer = Weapon("hammer", 2, 2, 0)
        self.assertEqual("sword", sword.getName())
        self.assertEqual(False, sword.isMagic())


if __name__ == "__main__":
    unittest.main()