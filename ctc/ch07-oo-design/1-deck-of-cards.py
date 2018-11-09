"""
Design the data structures for a generic deck of cards.
"""

from abc import ABC, abstractmethod


ACCEPTABLE_NUMBERS = [
    '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'
]

ACCEPTABLE_HOUSES = [
    'Diamond', 'Heart', 'Club', 'Spade'
]


class AbstractCard(ABC):
    """Enforces interface of Card abstraction"""
    @property
    @abstractmethod
    def number(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def house(self):
        raise NotImplementedError


class Card(AbstractCard):
    """Concrete Card object"""
    def __init__(self, number, house):
        self._number = number
        self._house = house

    def __repr__(self):
        return str({self._house: self._number})

    @property
    def number(self):
        return self._number

    @property
    def house(self):
        return self._house


class Deck:
    """
    A deck is composed of a full set of acceptable combinations
        of cards
    """
    def __init__(self):
        self._deck = []
        for house in ACCEPTABLE_HOUSES:
            for number in ACCEPTABLE_NUMBERS:
                self._deck.append(Card(number, house))

    def __len__(self):
        return len(self._deck)

    def __repr__(self):
        return str(self._deck)


if __name__ == "__main__":
    d = Deck()
    print(len(d))
    print(d)