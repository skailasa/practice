"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1
as one sorted array.

Note:
The number of elements initialized in nums1 and nums2 are m and n
respectively.
You may assume that nums1 has enough space (size that is greater or
equal to m + n) to hold additional elements from nums2.

Strategy:
Iterate through both lists, compare values until
"""
from typing import List


def merge(nums1: List[int], nums2: List[int])->None:
    """Merges nums2 into nums1 in-place"""

    merged = False
    i = 0
    j = 0
    nums1.append(9999)

    while not merged:

        if nums1[i] <= nums2[j]:
            i += 1

        elif nums1[i] > nums2[j]:
            nums1.insert(i, nums2[j])
            j += 1

        if j == len(nums2):
            merged = True

    nums1.pop()


if __name__ == "__main__":
    l1 = [1]
    l2 = [4, 5, 6, 7]

    merge(l1, l2)

    print(l1)