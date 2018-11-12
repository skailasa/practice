"""
Can also define a singleton using a decorator, by wrapping a class
in another class. a 'Class Decorator'
"""

class SingletonDecorator:
    
    def __init__(self, klass):
        self.klass = klass
        self.instance = None
    
    def __call__(self, *args, **kwargs):
        if self.instance == None:
            self.instance = self.klass(*args, **kwargs)
        return self.instance

class Foo:
    pass

def main():
    foo = SingletonDecorator(Foo)
    x = foo()
    y = foo()

    x.val = 'a' # this doesn't generally work on instances, but does on classes
    y.val = 'b'
    print(x.val)
    print(y.val)
    print(x is y)
    print(x.__dict__)

if __name__ == "__main__":
    main()
