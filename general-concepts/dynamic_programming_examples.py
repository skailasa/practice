"""
Various dynamic implementations of the fibonacci sequence calculation
"""


def recursive_fib(n):
    """
	Recursive implementaion of fibonacci calculation
		- O(2^n) - exponential complexity
	"""
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return recursive_fib(n - 1) + recursive_fib(n - 2)


def memoize(f):
    """
	Can cleverly choose to cache certain calls for fib
		to avoid calculating some values multiple times.
	"""
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]

    return helper


@memoize
def fib_memoized(n):
    """
	Results in complexity reducing to O(n) in time, as there can't 
		really be more than this many calls by definition. 
	"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib_memoized(n - 1) + fib_memoized(n - 2)


def iterative_fib(n):
    """
	Instead of recursion, can solve the problem iteratively
		Using the bottom-up way of thinking
	"""
    a, b = 0, 1

    for i in range(2, n):
        a, b = b, a + b

    return a + b


if __name__ == "__main__":
    from time import time

    n = 10

    a = time()
    fib_memoized(n)
    b = time()

    memoized_time = b - a

    c = time()
    recursive_fib(n)
    d = time()

    recursive_time = d - c

    e = time()
    iterative_fib(n)
    f = time()

    iterative_time = d - c

    print(
        "The memoized method is {} times faster than the recursive method".format(
            recursive_time / memoized_time))
    print(
        "The iterative method is {} times faster than the recursive method".format(
            recursive_time / iterative_time))
