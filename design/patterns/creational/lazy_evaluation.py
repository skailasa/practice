"""
Avoids the evaluation of a value till it's actually needed

pros:
    - can define control flow structures as abstractions rather than
    primitves as data won't actually flow through them
    - can define at least potentially infinite data structures
    - performance (compute) is increased by avoiding needless calculation

Often combined with memoisation:
    After a function's value is computed for that parameter or set of
    parameters, the result is stored in a lookup table that is indexed
    by the values of those parameters
"""

import functools

class lazy_property:

    def __init__(self, function):
        self.function = function
        functools.update_wrapper(self, function)

    def __get__(self, obj, owner):
        if obj is None:
            return self
        val = self.function(obj)
        obj.__dict__[self.function.__name__] = val
        return val


def lazy_property_2(fn):
    
    attr = '_lazy__' + fn.__name__
    
    @property
    def _lazy_property(self):
        if not hassattr(self, attr):
            setattr(self, attr, fn(self))
        return getattr(self, attr)
    return _lazy_property


class Person:

    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation
        self.call_count2 = 0

    @lazy_property
    def relatives(self):
        # get all relatives of a person, assume it takes a long time
        relatives = "all relatives" # 'algorithm to return relatives'
        return relatives

    
    @lazy_property_2
    def find_parents(self):
        parents = "mother + father"
        return parents


def main():
    sri  = Person("Sri", "Programmer")
    print("Name: {} Occumation: {}".format(sri.name, sri.occupation))
    print("Before accessing relatives")
    print(sri.__dict__)
    print("Sri's relatives: {}".format(sri.relatives))
    print("After we've accessed relatives")
    print(sri.__dict__)


if __name__ == "__main__":
    main()

