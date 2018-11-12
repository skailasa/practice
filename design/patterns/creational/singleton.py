"""
Provides only one object of a particular type.
Take control of object creation away from programmer.

A way to do this is to delegate to a single instance of a private
nested inner class.

The inner class is named with a double underscore, it is private
so the user hasn't got direct access to it. It contains all the 
methods you would normally put in the class, and wrapped in the
outer class which controls creation by using its own constructor.
The first time you only create an OnlyOne, it initialises the
instance, after that it just ignores you and sets the attribute val

Access comes through delegation, using the __getattr_() method to
redirect calls to the single instance
"""

class OnlyOne:
    
    class __OnlyOne:
        def __init__(self, arg):
            self.val = arg
        def __str__(self):
            return repr(self) + self.val

    instance = None
    
    def __init__(self, arg):
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne(arg)
        else:
            OnlyOne.instance.val = arg

    def __getattr__(self, name):
        return gettattr(self.instance, name)
