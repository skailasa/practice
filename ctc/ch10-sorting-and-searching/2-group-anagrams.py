"""
Write a method to sort an array of strings so that all the anagrams are
next to one another.

Strategy:
- mark anagrams with the same integer
- sort list of integers
"""


class Anagram:

    def __init__(self, A):
        self.A = A
        self.ledger = {}

    def check_anagram(self, a, b):
        sa = set([i for i in a])
        sb = set([i for i in b])
        return sa == sb

    def mark_anagrams(self):
        idx = 0
        for i, a in enumerate(self.A):
            remaining_list = self.A[:i] + self.A[i+1:]

            for j, b in enumerate(remaining_list):

                if self.check_anagram(a, b):
                    if {a, b} not in self.ledger.values():
                        self.ledger[idx] = {a, b}
                        idx += 1
                else:
                    pass

if __name__ == "__main__":
    A = ['irs', 'a', 'a', 'sri','hen', 'enh']

    a = Anagram(A)
    a.mark_anagrams()
    print(a.ledger)