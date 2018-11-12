"""
The factory method can be used to create an interface for a method,
leaving the implementation to the class that gets instantiated

i.e. we might not always know what kind of objects we want to create
in advance. Some objects can only be created at execution time after
a user requests to do so for example

A factory method solves this problem, it 'manufactures' a class
"""

def get_localiser(language):
    """factory method"""
    languages = dict(English=EngGetter, Hindi=HindiGetter)
    return languages[language]()  # instantiate an object upon execution


class HindiGetter:

    def __init__(self):
        self.trans = dict(dog="कुत्")

    def get(self, msgid):
        """Just return if there is no translation"""
        return self.trans.get(msgid, str(msgid))


class EngGetter:
    """Echoes the msg ids"""

    def get(self, msgid):
        return str(msgid)


def main():
    # create localiser 
    e, h = get_localiser(language="English"), get_localiser(language="Hindi")
    # translate some text
    for msgid in "dog cat".split():
        print(e.get(msgid), h.get(msgid))


if __name__ == "__main__":
    main()
