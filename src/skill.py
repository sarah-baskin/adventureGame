'''
This houses the skill class and its related stuff
'''

class Skill:
    '''
    This class handles the creation of player skills

    Advtange is a number between 1 and 5
    Disadvantage is a number between 1 and 5
    '''

    def __init__(self,
                 name : str,
                 description : str,
                 advantage : int,
                 disadvantage : int):
        self.name = name
        self.description = description
        self.advantage = advantage
        self.disadvantage = disadvantage
    def get_name(self) -> str:
        '''
        Returns a skill's name. Raises a value error if no
        name has been supplied for the skill
        '''
        if not self.name:
            raise ValueError('''To be named is to be known.
                             This skill must have a name.''')
        return self.name
    def get_description(self) -> str:
        '''
        Returns the description of a given skill.
        Raises a value error if no description has been provided
        to accurately describe the skill.
        '''
        if not self.description:
            raise ValueError('''What are words without definitions?
                             This skill must have a description''')
        return self.description
    def get_advantage(self) -> int:
        '''
        Returns the advantage level of the skill
        An int between 0-10
        '''
        return self.advantage
    def get_disadvantage(self) -> int:
        '''
        Returns the disadvantage level of the skill
        And int between 0-10
        '''
        return self.disadvantage
