"""
Design a call centre with 3 levels of employee: respondent, manager, director
- Incoming phone call must be first allocated to respondent, then manager, then director
depending on who's free
- Implement a method, dispatchCall() which assigns a call to first available employee
"""

from abc import ABC


class SingletonDecorator:
    """Define a class decorator to make Call Centre a singleton"""
    def __init__(self, klass):
        self.klass = klass
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self.klass(*args, **kwargs)
        return self.instance


class AbstractCallCentre(ABC):
    """
    Abstract Call Centre
    """

    def dispatch_call(self):
        raise NotImplementedError


# Make call centre a singleton as it doesn't make sense to have
# more than one
@SingletonDecorator
class CallCentre(AbstractCallCentre):
    """
    Concrete Call Centre
    """

    def __init__(self, ndirectors, nmanagers, nrespondents):
        self._employees = {}
        self._create_call_centre(ndirectors, nmanagers, nrespondents)

    def __repr__(self):
        return str(self._employees)

    def _create_call_centre(self, ndirectors, nmanagers, nrespondents):
        """Could theoretically have different functions in here"""
        self._employees.update(
            {
                "directors": Employee(navailable=ndirectors)
            }
        )

        self._employees.update(
            {
                'managers': Employee(navailable=nmanagers)
            }
        )

        self._employees.update(
            {
                'respondents': Employee(navailable=nrespondents)
            }
        )

    def _check_availablity(self, role):
        return self._employees[role]['available']

    def _mark_busy(self, role):

        if self._employees[role]['navailable'] > 0:
            self._employees[role]['navailable'] -= 1

        if self._employees[role]['navailable'] == 0:
            self._employees[role]['available'] = False

    def dispatch_call(self):
        if self._check_availablity('respondents'):
            self._mark_busy('respondents')

        elif self._check_availablity('managers'):
            self._mark_busy('managers')

        elif self._check_availablity('directors'):
            self._mark_busy('directors')

        else:
            raise ValueError('Call centre at full capacity')


class Employee:
    """Concrete Employee, separate from call centre implementation"""
    def __init__(self, navailable):
        self.available = True
        self.navailable = navailable

    @property
    def _employee(self):
        return {
            "available": self.available,
            "navailable": self.navailable,
        }

    def __repr__(self):
        return str(self._employee)

    def __getitem__(self, item):
        return self.__dict__[item]

    def __setitem__(self, key, value):
        self.__dict__[key] = value


if __name__ == "__main__":

    cc = CallCentre(ndirectors=1, nmanagers=2, nrespondents=3)

    print(cc)