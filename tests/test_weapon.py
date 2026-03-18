import unittest
from src.weapon import Weapon

class TestWeapon(unittest.TestCase):

    def test_sword(self):
        sword = Weapon("sword", 4, 3, False)
        self.assertEqual("sword", sword.getName())
        self.assertEqual(False, sword.isMagic())
    
    def test_hammer(self):
        hammer = Weapon("hammer", 2, 2, False)
        self.assertEqual("hammer", hammer.getName())
        self.assertEqual(False, hammer.isMagic())
    
    def test_staff(self):
        staff = Weapon("staff", 6, 8, True)
        self.assertEqual("staff", staff.getName())
        self.assertEqual(True, staff.isMagic())

if __name__ == "__main__":
    unittest.main()