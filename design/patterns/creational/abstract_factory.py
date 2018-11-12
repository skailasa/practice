"""
Provide an interface for creating families of dependent objects without
specifying their concrete classes.

Clients never create platform objects directly, they ask the factory to
do it for them.
Therefore exchanging product families is easy because the specific class
of the factory object appears only once in the application, when its 
instatiated. The application can wholesale replace the entire family of
products simply by instantiating a different concrete instance of the
abstract factory. Often implemented as a singleton.

- The abstract factory defines a factory method per product. Each factory
method creates a concrete product class, each concrete class is modelled with
a factory derived class.

reference: https://sourcemaking.com/design_patterns/abstract_factory
e.g. sheet metal stamping equipment used in the manufacture of cars.
The stamping equipment is the abstract factory which creates auto body
parts, the same equipment is used to stamp right *and* left handed doors,
rear and front bumpers etc for different models of cars
"""

class AbstractCarFactory():
    """An abstract car factory"""
    
    def __init__(self, car_factory):
        self.car_factory = car_factory

    @property
    def colour(self):
        return self.car_factory().colour 
    
    def __str__(self):
        return self.car_factory().__str__()


class RedCar:
    """Concrete Factory"""
    
    @property
    def colour(self):
        return "Red"
    
    def __str__(self):
        return "Big Red Car"

class Tesla:
    """Concrete Tesla factory"""

    @property
    def colour(self):
        return "Black as the night"
    
    def __str__(self):
        return "I'm a car for rich douchebags"


if __name__ == "__main__":
    red_car = AbstractCarFactory(RedCar)
    print(red_car)
    print(red_car.colour)
    
    tesla = AbstractCarFactory(Tesla)
    print(tesla)
    print(tesla.colour)

