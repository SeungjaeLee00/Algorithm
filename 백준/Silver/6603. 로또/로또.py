from itertools import combinations

while True:
	num = list(map(int, input().split()))

	k = num[0]
	arr = num[1:]
	if k == 0:
		break

	for comb in combinations(arr, 6):
		for i in comb:
			print(i, end=' ')
		print()
	print()