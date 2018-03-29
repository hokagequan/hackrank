
def plus_minus(arr):
	count = len(arr)
	positive, negative, zero = 0, 0, 0
	for x in arr:
		positive += 1 if x > 0 else 0
		negative += 1 if x < 0 else 0
		zero += 1 if x == 0 else 0
	return ('%.5f'%(positive / count), '%.5f'%(negative / count), '%.5f'%(zero / count))

def better_plus_minus(arr):
	n = len(arr)
	print(round(len([x for x in arr if x > 0])/n, 5))
	print(round(len([x for x in arr if x < 0])/n, 5))
	print(round(len([x for x in arr if x == 0])/n, 5))

if __name__ == '__main__':
	arr = [-4, 3, -9, 0, 4, 1]
	result = plus_minus(arr)
	better_plus_minus(arr)