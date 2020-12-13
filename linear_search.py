"""
Linear search, most basic search algorithms that goes through every element 
of the array to find the target.

Time Complexity - O(N)
Space Complexity - O(1)
"""

import sys


def linear_search(array, target):
	"""
	Arguments: Array (The list of elements), target(search element)
	Returns: Index if found
	"""
	for index,element in enumerate(array):
		if element == target:
			return index
	return -1

if __name__ == '__main__':
	array = list(map(int,sys.argv[1].strip('[]').split(",")))
	target = int(sys.argv[2])
	print(linear_search(array,target))