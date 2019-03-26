"""

"""


class Animal:
    """Abstract creator"""
    def __init__(self, sound):
        self.sound = sound

    def __call__(self, *args, **kwargs):
        print("This animal ", self.sound)


class Dog(Animal):
    """Concrete implementation of creator"""
    def __init__(self):
        super().__init__("barks")


ANIMALS = {
    "dog": Dog,
}


class AnimalSoundsFactory:
    """Product Factory"""

    def __init__(self, animal):
        self.animal = ANIMALS[animal]()

    def __call__(self, *args, **kwargs):
        self.animal()
