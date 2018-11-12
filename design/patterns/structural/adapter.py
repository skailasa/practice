"""
Provides a different interface for a class. E.g. a cable from abroad
needs an adaptor. Useful to integrate classes that couldn't be previously
integrated due to their incompatible interfaces.


- can wrap an existing class with a new interface
"""

class Dog:
    def __init__(self):
        self.name = "Dog"

    def bark(self):
        return "woof"


class Cat:
    def __init__(self):
        self.name = "Cat"

    def meow(self):
        return "meow"


class Human:
    def __init__(self):
        self.name = "Human"


    def speak(self):
        return "hello"


class Adapter:

    def __init__(self, obj, **adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        """All non-adapted calls passed to the object"""
        return getattr(self.obj, attr)

    def original_dict(self):
        """Original object dict"""
        return self.obj.__dict__


def main():
    
    animals = []
    dog = Dog()
    cat = Cat()
    human = Human()

    animals.append(Adapter(dog, make_noise=dog.bark))
    animals.append(Adapter(cat, make_noise=cat.meow))
    animals.append(Adapter(human, make_noise=human.speak))

    for animal in animals:
        print("The {} goes {}".format(animal.name, animal.make_noise()))


if __name__ == "__main__":
    print(main())


