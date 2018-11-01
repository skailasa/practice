"""
Bubble Sort implementation

The nested loops are always confusing for me, but really it's fairly simple.
One essentially goes through the list and first try and move the largest number
to the end, then the second largest to the end and so on. This means that you can
iterate over smaller sections of the list in the second loop as you go along.
"""

class Bubble:
    def sort(self, A):
        n = len(A)
        
        for i in range(n):
           for j in range(0, n-i-1):
               if A[j] > A[j+1]:
                   A[j], A[j+1] = A[j+1], A[j]
        print(A)
        return A 
    

if __name__ == "__main__":
    A = [100, 1, 2, 3, 4, 3]
    
    Bubble().sort(A)
