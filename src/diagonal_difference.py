import os
import sys

def diagonalDifference(a):
	count = len(a)
	value = 0
	for i in range(count):
		value += (a[i][i] - a[i][count-i-1])
	return abs(value)

if __name__ == '__main__':
	n = int(input())
	a = []

	for x in range(n):
		a.append(list(map(int, input().rstrip().split())))

	result = diagonalDifference(a)
	print(result)