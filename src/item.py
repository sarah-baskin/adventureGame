class Item:
    '''
    Items are objects that are contained in rooms and can be picked up and used by the player
    '''

    def __init__(self,
                 name : str,
                 description : str
                 ):
        self.name = name
        self.description = description
    def get_name(self) -> str:
        '''
        Returns the name of a given item
        '''
        return self.name
    def get_description(self) -> str:
        '''
        Returns the description of a given item
        '''
        return self.description
    