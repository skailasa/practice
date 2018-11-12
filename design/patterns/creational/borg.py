"""
If you wanted a Singleton to have a single set of state data for all
objects. That is you could create as many objects as you want, as long
as they refer to the same state information then you achieve the effect
of a Singleton. This is done with a Borg
"""

class Borg:
    
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class Singleton(Borg):

    def __init__(self, arg):
        Borg.__init__(self)
        self.val = arg

    def __str__(self):
        return self.val

def main():
    i1 = Singleton('srinath')
    
    print(i1.__dict__)
    i2 = Singleton('kailasa')

    print(i1.__dict__)
    print(i2.__dict__)

if __name__ == "__main__":
    main()
