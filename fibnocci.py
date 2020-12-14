"""
Program to find the nth fibnocci number
Time Complexity - O(2^n)
Space Complexity - O(1)
"""

import sys

def fibnocci(n):
	"""
	Recursive funtion to calculate a number in fibnocci
	"""
	if n==1 or n==0:
		return n

	return fibnocci(n-1) + fibnocci(n-2)


if __name__ == '__main__':
	n = int(sys.argv[1])
	print(fibnocci(n))