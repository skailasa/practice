"""
Implement an algorithm to determin if a string has all
unique characters.

Bonus: What if you can't use additional datastructures?
"""

from collections import Counter

class isUnique:

	def check_hashmap(self, string):
		"""
		Solution uses additional Counter (hashmap) datastructure
		"""
		c = Counter()
		for ch in string:
			c[ch]+=1

		for key in c.keys():
			if key > 1:
				return True

		return False

	def check_no_ds(self, string):
		"""
		Solution without using any additional datastructures
		"""
		if len(string) == 1:
			return True

		for i in range(len(string)):
			temp = string[i]
			substring = string[:i] + string[i+1:]
			for temp_ch in substring:
				if temp == temp_ch:
					return False

		return True



if __name__ == "__main__":
	print(isUnique().check_no_ds('abc'))