"""
Used when object creation is computationally expensive.
They are frequently created but only few are used at a time.

- cost of instantiation high
- rate of instantiation high
- number of instantiations low

It is possible to skip the costly creation of an object if one
is available in the pool. Allows for the checkout of an inactive
object and then to return to it. If none are available in the pool
it creates one.

If objects are reusable, it's desirable to keep these in the same pool,
these are often modelled using a singleton
"""

import queue


class ObjectPool(object):
    
    def __init__(self, queue, auto_get=False): 
        self._queue = queue
        if auto_get:
            self.item = self._queue.get()
        else:
            self.item = None
    
    def __enter__(self):
        if self.item is None:
            self.item = self._queue.get()
        return self.item

    def __exit__(self, Type, value, traceback):
        if self.item is not None:
            self._queue.put(self.item)
            self.item = None

    def __del__(self):
        if self.item is not None:
            self._queue.put(self.item)
            self.item = None


def main():

    sample_queue = queue.Queue()
    sample_queue.put('yam')

    with ObjectPool(sample_queue) as obj:
        print("Inside with: {}".format(obj))  # releases back to pool
    print("Outside with: {}".format(sample_queue.get()))  # reused with explicit get call
    

if __name__ == "__main__":
    main()
