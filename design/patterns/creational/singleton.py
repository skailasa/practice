"""
Implementation of a singleton in Python

- Single instance of a 'Global' object
- Some people consider it an anti-pattern
- Apparently can make testing difficult in some cases
    - though I can't really think of how...
"""

class Singleton:
    
    _instance = None

    class _Singleton:
        def __init__(self, arg):
            self.val = arg
        
        def __repr__(self):
            return str(self) + self.val

    def __init__(self, arg):
        if not Singleton._instance:
            Singleton._instance = Singleton._Singleton(arg)
        else:
            Singleton._instance.val = arg

    def __getattr__(self, name):
        return getattr(self._instance, name)

