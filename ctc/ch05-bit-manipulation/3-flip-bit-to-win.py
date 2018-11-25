"""
You have an integer and you can flip exactly one bit fro a 0 to a 1.
    Write code to find the length of the longest sequence of 1s you
    could create.

Strategy:
    - Check first bit value, if it's one begin count for longest seq.
    - iterate starting at first bit value
        - check following bit value, if it's a 1 add to longest seq
        - if current bit value is a 1, and 2 values hence is a 1 i.e.
        a single zero separating two ones, add 1 to to longest seq
        - otherwise, if it doesn't fit either of these patterns
            update current to previous longest.
"""


def check_current_bit_1(num):
    if (num & 1) & 1 == 1:
        return True
    return False


def longest_sequence(num):

    current_longest = 0
    previous_longest = 0

    if check_current_bit_1(num):
        current_longest += 1

    while num != 0:
        if check_current_bit_1(num >> 1):
            current_longest += 1

        elif check_current_bit_1(num) and check_current_bit_1(num >> 2):
            # if 1 followed by zero followed by a one add 1
            current_longest += 1

        else:
            # if zero is not followed by a 1 update
            if current_longest > previous_longest:
                previous_longest = current_longest
            current_longest = 0

        num = num >> 1

    return max(current_longest, previous_longest)


if __name__ == "__main__":

    num = 567
    print(bin(num))
    print(longest_sequence(num))
