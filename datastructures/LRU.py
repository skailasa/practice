"""
Implement an LRU Cache.

usage:

>>> cache = LRUCache(2)
>>> cache.put(1, 1)
>>> cache.put(2, 2)  # now filled to capacity
>>> cache.get(3)  # not a valid key
-1
>>> cache.put(3, 3)  # evicts 1

strategy:
- should use a stack to place items on
-


["LRUCache","put","get","put","get","get"]
[[1],[2,1],[2],[3,2],[2],[3]]
"""


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self._cache = []
        self._usage = []

    def __len__(self):
        return self.capacity

    @property
    def occupancy(self):
        return len(self._cache)

    def get(self, key: int) -> int:
        for item in self._cache:
            if key in item.keys():
                # update usage order
                if key in self._usage:
                    self._usage.remove(key)
                self._usage.append(key)

                return item[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if self.occupancy < self.capacity:
            self._cache.append({key: value})

        else:
            # evict least recently used item
            key_to_pop = self._usage[0]
            for idx, item in enumerate(self._cache):
                if key_to_pop in item.keys():
                    self._cache.pop(idx)

            self.put(key, value)


if __name__ == "__main__":
    cache = LRUCache(1)

    cache.put(2, 1)
    print(cache.get(2))
    cache.put(3, 2)
    print(cache.get(2))
    print(cache.get(3))



