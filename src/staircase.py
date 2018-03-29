import os
import sys

def stairecase(n):
	for i in range(0,n):
		print(" "*(n - i - 1) + "#" * (i + 1))

def better_staircase(n):
	[print(("#"*f).rjust(n)) for f in range(1,n+1)]

if __name__ == '__main__':
	n = int(input())
	# stairecase(n)
	better_staircase(n)