def birthday_cake_candles(arr):
    max_values_count = 0
    max_value = 0
    for x in arr:
    	if x > max_value:
    		max_value = x
    		max_values_count = 1
    	elif x == max_value:
    		max_values_count += 1
    print(max_values_count)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    birthday_cake_candles(arr)
