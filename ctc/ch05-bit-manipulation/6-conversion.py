"""
Write a function to determine the number of bits you need to flip to
    convert integer A to B.

e.g.
    29 (11101) to 15 (01111)
    ans: 2

Strategy, just need to find where result of & is 0
"""


def check_current_bit_1(num):
    if (num & 1) & 1 == 1:
        return True
    return False


def number_of_flips(num1, num2):

    res = num1 & num2
    count = 0

    while res != 0:
        if check_current_bit_1(res):
            count += 1

        res = res >> 1

    return count


if __name__ == "__main__":
    n1 = 15
    n2 = 25

    print(number_of_flips(n1, n2))