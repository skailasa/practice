"""
Implementation of Selection Sort
"""

class Selection:
    
    def find_smallest(self, A):
        
        smallest = A[0]
        idx_smallest = 0
        for i in range(len(A)):
            if A[i] < smallest:
                smallest = A[i]
                idx_smallest = i
 
        return idx_smallest, smallest

    def swap_n_smallest(self, A, smallest, idx_smallest):
        
        A[0] = smallest
        A[idx_smallest] = A[0]
        
        return A

    def sort(self, A):
        
        for i in range(len(A)):
            idx_smallest, smallest = self.find_smallest(A[i:])  
            A[i], A[i+idx_smallest] = smallest, A[i]
        print(A)

if __name__ == "__main__":
    A = [4,100, 2, 1, 3]
    print(Selection().sort(A)) 
