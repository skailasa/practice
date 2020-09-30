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



class ConcreteA:
    """A concrete prototype"""
    value = 'A' 


class ConcreteB:
    """A concrete prototype"""
    value = 'B' 


PROTOTYPES = {'a': ConcreteA, 'b': ConcreteB}


class Prototype:
    """Declare an interface for a protoype"""
    value = 'default'

    def __init__(self, value):
        self.value = value
        self.clone(value=value)
        
    def clone(self, **attrs):
        """Clone a prototype and update inner attributes dict"""
        obj = PROTOTYPES[attrs['value']]()
        obj.__dict__.update(attrs)
        return obj


def main():
    prototype = Prototype('a')
    print(prototype.value) 


if __name__ == "__main__":
    main()
