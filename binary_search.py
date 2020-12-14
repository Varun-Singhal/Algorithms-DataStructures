"""
Binary search algorithm
Time Complexity = O(logN)
Space Complexity = O(N)
"""
import sys

def binary_search(array, target):
	"""
	Arguments : Array(list), target(element to find)
	Returns: Index if found, -1 otherwise
	"""
	low = 0
	high = len(array)-1

	while(low<=high):
		mid = (low+high)//2
		if array[mid] == target:
			return mid
		elif array[mid] < target:
			low = mid+1
		else:
			high = mid-1

	return -1


if __name__ == "__main__":
	array = list(map(int,sys.argv[1].strip('[]').split(",")))
	target = int(sys.argv[2])
	print(binary_search(array,target))