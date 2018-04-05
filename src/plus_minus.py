import os
import sys

def plus_minus(arr):
	count = len(arr)
	positve, negative, zero = 0, 0, 0
	for x in arr:
		positve += (1 if x > 0 else 0)
		negative += (1 if x < 0 else 0)
		zero += (1 if x == 0 else 0)
	return (positve/count, negative/count, zero/count)


if __name__ == '__main__':
	arr = [-4, 3, -9, 0, 4, 1]
	result = plus_minus(arr)
	print(result)