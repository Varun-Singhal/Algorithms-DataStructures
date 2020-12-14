"""
Buubble sort algorithm 
Time Complexity - O(N)
Space Complexity- O(1)
"""
import sys

def bubble_sort(array):
	"""
	Function to perform bubble sort
	Argument: Unsorted Array
	Returns : Sorted Array
	"""
	updated = 1
	counter = 0

	while(updated == 1):
		updated = 0
		
		for i in range(len(array)-1-counter):
			if array[i] > array[i+1]:
				array[i],array[i+1] = array[i+1],array[i]
				updated = 1
		
		counter += 1

	return array 

if __name__ == '__main__':
	array = list(map(int,sys.argv[1].strip("[]").split(",")))
	print(bubble_sort(array))