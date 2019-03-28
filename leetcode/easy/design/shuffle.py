"""
Shuffle the array [1,2,3] and return its result.
Any permutation of [1,2,3] must equally likely to be returned.

solution.shuffle();

Resets the array back to its original configuration [1,2,3].
solution.reset();

Returns the random shuffling of array [1,2,3].
solution.shuffle();
"""
from random import sample
from typing import List


class Shuffle:
    def __init__(self, nums: List[int]):
        self._nums = nums

    def reset(self):
        return self._nums

    def shuffle(self):
        return sample(self._nums, k=len(self._nums))


if __name__ == "__main__":
    s = Shuffle([1, 2, 3])

    print(s.shuffle())

    print(s.reset())
