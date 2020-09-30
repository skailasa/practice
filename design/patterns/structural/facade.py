"""
Intent: Provide a unified interface to a set of interfaces encapsulated in a
`subsystem`. Useful for weakly coupling two systems.
"""

class Reader:
    """System 1
    """
    def read(self):
        print("reading")


class Writer:
    """System 2
    """
    def write(self):
        print("writing")


class Student:
    """Facade
    """
    def __init__(self):
        self.reader = Reader()
        self.writer = Writer()

    def study(self):
        self.reader.read()
        self.writer.write()


class Client:
    """Actor
    """
    def __init__(self):
        self.student = Student()

    def __call__(self):
        self.student.study()


if __name__ == "__main__":

    c = Client()
    c()
