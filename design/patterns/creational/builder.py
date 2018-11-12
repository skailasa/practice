"""
Decouple complex objects construction from their representation.
So that same process can be reused to build objects from the same
family

Useful to separate specification of an object from its actual
representation.

Can do this using abstract base classes

reference: https://sourcemaking.com/design_patterns/builder
Check List:
    1. decide if a common input and many possible representations
    exist for the problem at hand
    2. Encaspsulate parsing of a common input in a reader class
    3. Design a standard protocol for all representations in a builder
    base class
    4. define a derived builder class for each target representation
    5. The client creates a Reader object and a Builder object
    registering the latter with the former
    6. The client asks the Reader to construct
    7. The client asks the Builder to return the result
"""

from abc import ABC
from abc import abstractmethod


class AbstractBuilding(ABC):
    """
    Abstract Builder
    """
    
    name = NotImplemented

    def __init__(self):
        self.build_floor()
        self.build_size()

    @abstractmethod
    def build_floor(self):
        raise NotImplementedError
    
    @abstractmethod
    def build_size(self):
        raise NotImplementedError

    def __repr__(self):
        return "Floor: {0.floor} | Size: {0.size}".format(self)


class House(AbstractBuilding):
    """Concrete House Builder"""    
   
    name = 'house'
    
    def build_floor(self):
        self.floor = '2'
    
    def build_size(self):
        self.size = 'big'


class Flat(AbstractBuilding):
    """Concrete Flat Builder"""
    
    name = 'flat'

    def build_floor(self):
        self.floor = 1

    def build_size(self):
        self.size = 'small'


class Director:
    """Director, which is called by the client calls consistent interface"""
    building_types = {
        'flat': Flat,
        'house': House
    }
    
    def construct_building(self, building_type):
        return self.building_types[building_type]()


if __name__ == "__main__":
    
    flat = Director().construct_building('flat')
    house = Director().construct_building('house')

    print(flat.name)
    print(flat)
