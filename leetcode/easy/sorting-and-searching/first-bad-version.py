"""
You are a product manager and currently leading a team to develop a new
product. Unfortunately, the latest version of your product fails the
quality check. Since each version is developed based on the previous
version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the
first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether
version is bad. Implement a function to find the first bad version.
You should minimize the number of calls to the API.

Strategy:
- binary search for a bad version, then iterate forwards to find first
one.
"""


def api_response(i):
    """Mock api response"""

    if i <= 4:
        return True

    return False


def first_bad_version(n):

    mid = n // 2

    if api_response(mid):
        # iterate forward
        tmp = None
        for i in range(mid, n):
            if api_response(i):
                tmp = i
        print("first bad version: ", tmp)

    else:
        first_bad_version(n//2)


if __name__ == "__main__":
    n = 10
    first_bad_version(n)
