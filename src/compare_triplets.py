
def solve(a0, a1, a2, b0, b1, b2):
	a_point, b_point = 0, 0
	a_data = [a0,a1,a2]
	b_data = [b0,b1,b2]

	for i in range(0, 3):
		if a_data[i] > b_data[i]:
			a_point += 1
		elif a_data[i] < b_data[i]:
			b_point += 1
            
	return [a_point, b_point]

def better_solve(a0, a1, a2, b0, b1, b2):
	a_point = (1 if a0 > b0 else 0) + (1 if a1 > b1 else 0) + (1 if a2 > b2 else 0)
	b_point = (1 if b0 > a0 else 0) + (1 if b1 > a1 else 0) + (1 if b2 > a2 else 0)
	return (a_point, b_point)

if __name__ == '__main__':
	result = better_solve(5,6,7,3,6,10)
	print(result)