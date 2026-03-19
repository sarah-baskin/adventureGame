import unittest
from src.skill import Skill

class TestSkills(unittest.TestCase):

    def test_with_name_and_description(self):
        magic = Skill("magic", 
                          "ability to cast spells",
                          2,
                          0)
        self.assertEqual("magic", magic.get_name())
        self.assertEqual("ability to cast spells", magic.get_description())
    
    def test_without_name(self):
        no_name = Skill("", 
                          "ability to cast spells",
                          2,
                          0)
        with self.assertRaises(ValueError):
            no_name.get_name()
    
    def test_without_description(self):
        no_desc = Skill("communication", 
                          "",
                          3,
                          0)
        with self.assertRaises(ValueError):
            no_desc.get_description()
