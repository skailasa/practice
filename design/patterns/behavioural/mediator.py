"""
Decouple complex class interactions using a mediator. Removes dependency
between different components.
"""


class Mediator:
    """
    Declares a method for use by components to notify mediator about events,
        the mediator can then choose whether or not to react to these events,
        and in general how to handle them.
    """
    def notify(self, sender, event):
        pass


class ConcreteMediator(Mediator):

    def __init__(self, c1, c2):
        # Instatiate with objects it mediates between, set the mediator for
        # these objects.
        self.c1 = c1
        self.c1.mediator = self
        self.c2 = c2
        self.c2.mediator = self

    def notify(self, sender, event):
        if event == 'A':
            print("Mediator reacts on A and triggers following operations:")
            self.c1.do_b()

        elif event == 'C':
            print("Mediator reacts on B and triggers following operations:")
            self.c2.do_d()


class Component:
    def __init__(self, mediator=None):
        self.mediator = mediator


"""
Concrete components implement some complex functionality that we don't want
to interact.
"""


class ComponentOne(Component):

    def do_a(self):
        self.mediator.notify(self, "A")

    def do_b(self):
        print('doing b')


class ComponentTwo(Component):

    def do_c(self):
        self.mediator.notify(self, "C")

    def do_d(self):
        print('doing d')


if __name__ == "__main__":
    # The client code.
    c1 = ComponentOne()
    c2 = ComponentTwo()
    mediator = ConcreteMediator(c1, c2)

    print("Client triggers operation A.")
    c1.do_a()

    print("Client triggers operation D.")
    c2.do_c()
