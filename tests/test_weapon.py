import unittest
from src.weapon import Weapon

class TestWeapon(unittest.TestCase):

    def test_sword(self):
        sword = Weapon("sword", 4, 3, False)
        self.assertEqual("sword", sword.get_name())
        self.assertEqual(False, sword.get_sorcery())
    
    def test_hammer(self):
        hammer = Weapon("hammer", 2, 2, False)
        self.assertEqual("hammer", hammer.get_name())
        self.assertEqual(False, hammer.get_sorcery())
    
    def test_staff(self):
        staff = Weapon("staff", 6, 8, True)
        self.assertEqual("staff", staff.get_name())
        self.assertEqual(True, staff.get_sorcery())

if __name__ == "__main__":
    unittest.main()