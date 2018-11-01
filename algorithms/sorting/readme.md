# Sorting Algorithms

Of those asked in interviews, merge sort, quick sort, and bucket sort are the most common.

## Bubble Sort
- Start at beginning of array and swap two elements if the first greater than the second
- Do so for next pair, continuously sweeping the array until it's sorted.
- Smaller items slowly 'bubble' to beginning of array.
- Runtime O(N^2), average and worst case. Memory O(1) - Only have to keep two values in memory.

## Selection Sort
- Simple and inefficient
- Find the smallest element using a linear scan, and swap with first element
- Find the second smallest, and repeat etc.
- Runtime O(N^2) average and worst case. Memory O(1)

## Merge Sort
- Divides array in half, sorting each half, and merging back together
- Each half has same algorithm applied to it
- Eventually just merging two single element arrays
- Runtime O(nlog(n)) average and worst case, Memory is array/algorithm dependent

- Follows the Divide and Conquer paradigm
- Divide: n-element sequence to be sorted into two subsequences of n/2 elements each
- Conquer: Recursively sort two subsequences using Merge-Sort
- Combine: Merge to subsequences to produce final solution


## Quick Sort


## Radix Sort
 
