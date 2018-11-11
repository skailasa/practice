"""
A child running up a staircase with N steps
- They can hop 1, 2 or 3 steps at a time
- Find a method to calculate the number of ways
they can run up the stairs.
"""


def memoize(func):
    """Memoize the recurive call with a decorator"""
    memo = {}

    def wrapper(self, x):
        if x not in memo:
            return func(self, x)
        return memo[x]

    return wrapper


class Steps:
    """
    Recursively calculate the number of steps using the base case
        - Using the piece of knowledge that if you're on the last
        step the 'number of routes' is only 1
        - From this last step you have 3 choices.
    """

    @memoize
    def number_of_routes(self, n):
        if n < 0:
            return 0
        elif n == 0:
            return 1
        else:
            return self.number_of_routes(n-1) + self.number_of_routes(n-2) + self.number_of_routes(n-3)


if __name__ == "__main__":
    print(Steps().number_of_routes(10))

