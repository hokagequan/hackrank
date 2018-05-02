import sys
import itertools

def divisible_sum_pairs(n, k, ar):
	if len(ar) <= 1:
		return 0

	count = 0
	base_value = ar.pop(0)
	for i in range(0, len(ar)):
		value = ar[i]
		count += 1 if (base_value + value) % k == 0 else 0

	count += divisible_sum_pairs(n, k, ar)

	return count

def better(n, k, ar):
	return len([x for x in itertools.combinations(range(n), 2) if (ar[x[0]] + ar[x[1]]) % k == 0])

def better2(n, k, ar):
	nums = [0] * k
	count = 0
	for ele in ar:
		modu = ele % k
		print(f"{ele} {modu} {count} {nums} - after modu")
		count += nums[(k - modu) % k]
		print(f"{ele} {modu} {count} {nums} - after count+=")
		nums[modu] += 1
		print(f"{ele} {modu} {count} {nums} - after nums+=")
		print("-----------------------")
	return count

if __name__ == '__main__':
	n, k = input().strip().split(" ")
	n, k = [int(n), int(k)]
	ar = list(map(int, input().strip().split(" ")))
	# result = divisible_sum_pairs(n, k, ar)
	result = better2(n, k, ar)
	print(result)
