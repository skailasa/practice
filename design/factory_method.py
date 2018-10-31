"""
Creates an interface for the creation of an object, leaving
the implementation to the actual child class that gets
instantiated.

Can be implemented using abstract classes which impose the
interface.
"""


class Translator:
    """Factory for translation of a language"""
    def __init__(self, language):
        self._language = language
    
    def translate(self, phrase):
        LANGUAGES[self._language]().translate(phrase)

class HindiTranslator:
    lookup = {"dog": "कुत्"}

    def translate(self, phrase):
        print(HindiTranslator.lookup['dog'])


LANGUAGES = {"hindi": HindiTranslator}


def main():
    t = Translator('hindi')
    t.translate('dog')

if __name__ == "__main__":
    main()
