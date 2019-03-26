from abc import ABC
from abc import abstractmethod


class AbstractAlgorithm(ABC):
    """Abstract algorithm"""

    @abstractmethod
    def solve_equation(self):
        raise NotImplementedError


class ConcreteAlgorithm1(AbstractAlgorithm):
    """An example concrete implementation"""

    def solve_equation(self):
        return "solution method 1"


class ConcreteAlgorithm2(AbstractAlgorithm):
    """An example concrete implementation"""

    def solve_equation(self):
        return "solution method 2"


def client(method):
    """Client dynamically chooosed algorithm"""
    methods = {
        "one": ConcreteAlgorithm1,
        "two": ConcreteAlgorithm2,
    }

    return methods[method]().solve_equation()

