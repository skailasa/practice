"""
Consider this list [1, 2, 2, 3, 4, 5, 4, 5], one knows that all digits
    are repeated but for one particular digit - write a function (in
    linear time) to find this digit.

Solution achieved by understanding that there is no order of precedence
    in bitwise operations, much like addition/substraction.
"""


def solution(l):
    res = 0
    for num in l:
        res &= num

    return res


if __name__ == "__main__":
    print(solution([1,1,1,1,1,3,3,3,3,3]))
    print(solution([1,3]))

