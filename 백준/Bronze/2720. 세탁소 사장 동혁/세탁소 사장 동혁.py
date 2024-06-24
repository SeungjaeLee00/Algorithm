t = int(input())
# list = [int(input()) for i in range(t)]
for _ in range(t):
	money = int(input())
	for i in [25, 10, 5, 1]:
		print(money//i, end=' ')
		money = money%i