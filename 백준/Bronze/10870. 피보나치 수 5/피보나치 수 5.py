def fibo(x):
	# base case
	if x == 1:
		return 1
	if x == 0:
		return 0 

	# rescursive case
	return fibo(x - 1) + fibo(x - 2)

n = int(input())
print(fibo(n))