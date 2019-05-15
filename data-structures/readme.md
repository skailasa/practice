# Data Structures

## Linear Data Structures

A data structure is said to be linear if its elements form a linear list/sequence

e.g:

- Array
- Linked List
- Stack
- Queue

Operations Supported by linear data structures:

- Traversal, visit evert part of a data structure
- Search, find a given element by traversing a data structure
- Insertion, Add a new element
- Deletion, remove a given element
- Sorting, rearrange following some kind of order
- Merging, combine two data structures into one 


## Hash Tables
- In Python both sets and dictionaries are examples of hashtables. Collisions are inherent to these datastructures
as we can't guarantee that our hash will be unique. Can resolve collisions by using a linked list at each index. We just
add items to this linked list, as long as the number of collisions is fairly small this is stil fairly efficient, in the
worst case lookup is O(n) where n is the number of elements in the hash table.