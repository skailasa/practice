"""
Reduces the number of classes required by an application.
Instead of subclasses, creates objects by copying a prototypical
instance at runtime.

Easier to derive new kinds of objects, when instances of the class have
only a few different combinations of state, and when instantiation
is expensive

When the number of prototypes in an application can vary, it can be useful
keep a dispatcher (aka registry/manager). Allows clients to query the
dispatcher for a prototype before cloning a new instance.
"""


class Prototype:
    """Declare an interface for a protoype"""
    value = 'default'
     
    def __init__(self, name):
        self.name = name

    def clone(self, **attrs):
        """Clone a prototype and update inner attributes dict"""
        obj = _prototypes[self.name]()
        obj.__dict__.update(attrs)
        return obj

class ConcreteA:
    """A concrete prototype"""
    value = 'A' 
    
    def clone(self, **attrs):
        """Clone a prototype, returning a copy of ConcreteA()"""
        obj = self.__class__()
        obj.__dict__.update(attrs)
        return obj

class ConcreteB:
    """A concrete prototype"""
    value = 'B' 
    
    def clone(self, **attrs):
        """Clone a prototype, returning a copy of ConcreteA()"""
        obj = self.__class__()
        obj.__dict__.update(attrs)
        return obj

PROTOYPES = {'a': ConcreteA, 'b': ConcreteB}

def main():
    prototype = Prototype('a')
    prototype.value 


if __name__ == "__main__":
    main()
