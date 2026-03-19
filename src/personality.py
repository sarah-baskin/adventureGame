'''
This houses the skill class and its related stuff
'''

from abc import ABC
from typing import List, Optional

from src.skill import Skill
from src.weapon import Weapon


class Alignment(ABC):
    """Base class for player alignments.

    Each alignment comes pre-configured with a set of default skills and
    weapons, and can be extended with additional ones.
    """

    def __init__(
        self,
        name: str,
        skills: Optional[List[Skill]] = None,
        weapons: Optional[List[Weapon]] = None,
    ):
        self._name = name
        self._skills = skills or []
        self._weapons = weapons or []

    def get_name(self) -> str:
        '''
        Returns the name of the personality on the alignment chart
        '''
        return self._name

    def get_skills(self) -> List[Skill]:
        '''
        Returns the list of skills associated with a given alignment
        '''
        return list(self._skills)

    def get_weapons(self) -> List[Weapon]:
        '''
        Returns the list of weapons associated with a given alignment
        '''
        return list(self._weapons)

    def add_skill(self, skill: Skill) -> None:
        '''
        Adds a skill to an alignment option
        '''
        self._skills.append(skill)

    def add_weapon(self, weapon: Weapon) -> None:
        '''
        Adds a weapon to alignment option
        '''
        self._weapons.append(weapon)

class LawfulGood(Alignment):
    '''
    Corresponds to the Lawful Good alignment
    '''

    def __init__(self):
        super().__init__(
            name="Lawful Good",
            skills=[
                Skill("Justice", "Upholds the law and stands up for others", 4, 1),
                Skill("Honor", "Acts with integrity", 4, 1),
            ],
            weapons=[
                Weapon("Longsword", 6, 3, False),
            ],
        )


class LawfulNeutral(Alignment):
    '''
    Corresponds to the Lawful Good alignment
    '''

    def __init__(self):
        super().__init__(
            name="Lawful Neutral",
            skills=[
                Skill("Discipline", "Follows the rules without question", 2, 0),
            ],
            weapons=[
                Weapon("Spear", 4, 2, False),
            ],
        )


class LawfulEvil(Alignment):
    '''
    Corresponds to the Lawful Good alignment
    '''

    def __init__(self):
        super().__init__(
            name="Lawful Evil",
            skills=[
                Skill("Authority", "Uses systems to control others", 2, 0),
            ],
            weapons=[
                Weapon("Dagger", 3, 1, False),
            ],
        )


class NeutralGood(Alignment):
    '''
    Corresponds to the Lawful Good alignment
    '''

    def __init__(self):
        super().__init__(
            name="Neutral Good",
            skills=[
                Skill("Compassion", "Helps others out of kindness", 2, 0),
            ],
            weapons=[
                Weapon("Staff", 2, 2, True),
            ],
        )


class TrueNeutral(Alignment):
    '''
    Corresponds to the Lawful Good alignment
    '''

    def __init__(self):
        super().__init__(
            name="True Neutral",
            skills=[
                Skill("Balance", "Maintains equilibrium between extremes", 2, 0),
            ],
            weapons=[
                Weapon("Dagger", 2, 1, False),
            ],
        )


class NeutralEvil(Alignment):
    '''
    Corresponds to the Lawful Good alignment
    '''

    def __init__(self):
        super().__init__(
            name="Neutral Evil",
            skills=[
                Skill("Survival", "Does whatever it takes to stay alive", 2, 0),
            ],
            weapons=[
                Weapon("Club", 3, 2, False),
            ],
        )


class ChaoticGood(Alignment):
    '''
    Corresponds to the Lawful Good alignment
    '''

    def __init__(self):
        super().__init__(
            name="Chaotic Good",
            skills=[
                Skill("Freedom", "Breaks rules to do what’s right", 2, 0),
            ],
            weapons=[
                Weapon("Bow", 4, 1, False),
            ],
        )


class ChaoticNeutral(Alignment):
    '''
    Corresponds to the Lawful Good alignment
    '''

    def __init__(self):
        super().__init__(
            name="Chaotic Neutral",
            skills=[
                Skill("Adaptability", "Changes with the moment", 2, 0),
            ],
            weapons=[
                Weapon("Whip", 3, 1, False),
            ],
        )


class ChaoticEvil(Alignment):
    '''
    Corresponds to the Lawful Good alignment
    '''

    def __init__(self):
        super().__init__(
            name="Chaotic Evil",
            skills=[
                Skill("Anarchy", "Seeks chaos for its own sake", 2, 0),
            ],
            weapons=[
                Weapon("Axe", 5, 2, False),
            ],
        )
