"""
Given an infinite number of 25c, 10c, 5c and 1c coins, write code to
    calculate the number of ways of representing n-cents.
"""

DENOMINATIONS = [
    25, 10, 5, 1
]


def make_change(n, denominations, index):

    if index >= len(denominations)-1:
        # last denomination reached, there's only 1 way of constructing
        # change at this point
        return 1

    denom_amount = denominations[index]

    ways = 0

    i = 0
    while i*denom_amount <= n:
        remainder = n - i*denom_amount
        ways += make_change(remainder, denominations, index+1)
        i += 1

    return ways


if __name__ == "__main__":
    print(make_change(10, DENOMINATIONS, 0))

