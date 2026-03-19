class Item:
    '''
    Items are objects that are contained in rooms and can be picked up and used by the player
    '''

    def __init__(self,
                 name : str,
                 description : str,
                 takeable : bool
                 ):
        self.name = name
        self.description = description
        self.takeable = takeable
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
    def get_takeable(self) -> bool:
        '''
        Returns whether or not an item is takeable 
        (must it stay in this room or can it leave)
        '''
        return self.takeable

class Satchel(Item):
    '''
    Defines the workings of the satchel
    '''
    def __init__(self,
                 name : str,
                 description : str,
                 takeable : bool,
                 contains : list[Item]
                 ):
        self.name = name
        self.takeable = takeable
        self.description = description
        self.contains = contains
    def get_holding(self) -> list[Item]:
        return self.contains
    def add_to_holding(self,
                       obj : Item) -> None:
        self.contains.append(obj)
    def remove_from_holding(self,
                            obj: Item) -> None:
        self.contains.remove(obj)
    