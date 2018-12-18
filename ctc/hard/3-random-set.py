"""
Write a method to randomly generate a set of m integers from an array
    of size n. Each element must have an equal probability of being
    chosen.

Strategy:
    - Basically need to implement a random number generator to pick a
        random index.
"""

import random


def random_set(a, m):

    res = []
    while m > 0:

        # implement my own.
        random_index = random.randint(0, len(a)-1)


        random_choice = a[random_index]
        if random_choice not in res:

            res.append(a[random_index])
            m -= 1

    return res


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6]
    m = 3
    print(random_set(a, m))