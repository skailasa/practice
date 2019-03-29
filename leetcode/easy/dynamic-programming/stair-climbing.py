"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways
can you climb to the top?
"""


def memoize(func):
    """Memoize the recurive call with a decorator"""
    memo = {}

    def wrapper(x):
        if x not in memo:
            return func(x)
        return memo[x]

    return wrapper


@memoize
def number_of_ways(n):
    if n < 0:
        return 0

    if n == 0:
        return 1

    else:
        return number_of_ways(n-1) + number_of_ways(n-2)


if __name__ == "__main__":
    n_steps = 13
    print(number_of_ways(n_steps))