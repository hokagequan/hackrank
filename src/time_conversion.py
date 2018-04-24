from datetime import datetime

def time_conversion(s):
	dt = datetime.strptime(s, "%I:%M:%S%p")
	return dt.strftime("%H:%M:%S")

if __name__ == '__main__':
	s = input()
	result = time_conversion(s)
	print(result)