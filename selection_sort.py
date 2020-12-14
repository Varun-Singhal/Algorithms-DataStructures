"""
Selection Sort Algorithm
Time - O(N^2)
Space - O(1)

"""
import sys

def selection_sort(array):
	for i in range(len(array)-1):
		smallest_index = i

		for j in range(i+1,len(array)):
			if array[j]<array[smallest_index]:
				smallest_index = j
			
		array[i],array[smallest_index] = array[smallest_index],array[i]

	return array

if __name__ == '__main__':
	array = list(map(int,sys.argv[1].strip("[]").split(",")))
	print(selection_sort(array))