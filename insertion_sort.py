"""
Insertion sort algorithm 
Time Complexity - O(N^2)
Space Complexity- O(1)
"""
import sys

def insertion_sort(array):
	"""
	Function to perform bubble sort
	Argument: Unsorted Array
	Returns : Sorted Array
	"""
	for i in range(1,len(array)):
		index = i-1

		if array[i] < array[i-1]:
			swap(array,i,i-1)

		while(index>0):
			if array[index] < array[index-1]:
				swap(array,index,index-1)
			index -= 1

	return array 

def swap(array, i, j):
	array[i],array[j] = array[j],array[i]

if __name__ == '__main__':
	array = list(map(int,sys.argv[1].strip("[]").split(",")))
	print(insertion_sort(array))