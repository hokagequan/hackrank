import sys

def minimaxsum(arr):
	if len(arr) <= 1:
		return

	min_value = sys.maxsize
	max_value = 0
	for x in range(0, len(arr)):
		tmp = arr[:]
		del tmp[x]
		sum_value = sum(tmp)
		min_value = sum_value if sum_value < min_value else min_value
		max_value = sum_value if sum_value > max_value else max_value

	print("{} {}".format(min_value, max_value))

def better(arr):
	if len(arr) <= 1:
		return

	sum_value = sum(arr)
	print("{} {}".format((sum_value - max(arr)), (sum_value - min(arr))))


if __name__ == '__main__':
	arr = list(map(int, input().rstrip().split()))
	minimaxsum(arr)