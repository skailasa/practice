"""
Check two strings to decide if one is a permutation of the other
"""


class Perm:

    def __init__(self, s1, s2):
        """Initialise with strings being checked"""
        self.s1 = s1
        self.s2 = s2

    def _split(self, string):
        return [i for i in string]

    def check(self):
        """Use Python sets, hashes :)"""
        return bool(set(self._split(self.s1)) == set(self._split(self.s2)))


if __name__ == "__main__":
    print(Perm('sri', 'sir').check())  # True
