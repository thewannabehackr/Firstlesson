def fibonacci(n):
	if n == 0 or n == 1:
		return 1
	else:
		print('sum of {0} and {1}'.format(n-1,n-2))
		return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':

	print(fibonacci(10))
