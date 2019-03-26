
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
    d = Director()

    flat = d.construct_building('flat')
    house = d.construct_building('house')

    print(flat.name)
    print(flat)
